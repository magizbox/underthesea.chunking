from os.path import join

import pandas as pd
import os


class TaggedCorpus:
    def __init__(self, sentences=[]):
        self.sentences = sentences

    def save(self, filepath):
        sentences = self.sentences
        content = "\n\n".join(["\n".join(["\t".join(t) for t in s]) for s in sentences])
        open(filepath, "w").write(content.encode("utf-8"))

    def _parse_sentence(self, text):
        tokens = text.split("\n")
        tokens = [token.split("\t") for token in tokens if token.strip() != ""]
        return tokens

    def load(self, filepath):
        with open(filepath) as f:
            content = f.read().strip()
            content = content.decode("utf-8")
            sentences = content.split("\n\n")
            sentences = [self._parse_sentence(s.strip()) for s in sentences if s.strip() != ""]
            self.sentences = sentences

    def _analyze_field(self, df, id, output_folder="."):
        id = str(id)
        m = df.shape[1]
        df.columns = [str(i) for i in range(m)]

        df_temp = df.groupby(id)["0"].value_counts().groupby(level=0).nlargest(10).to_frame()
        tmp_filename = "tmp.xlsx"
        df_temp.to_excel(tmp_filename)
        df_temp = pd.read_excel(tmp_filename)
        df_temp[id] = df_temp[id].fillna(method="ffill")
        os.remove(tmp_filename)

        df_id = df_temp.groupby(id)["0"].apply(lambda g: ", ".join(g)).reset_index(name="0")

        df_count = df[id].value_counts().reset_index(name="count")
        df_count = df_count.rename(columns={"index": id})

        df_analyze = pd.merge(df_id, df_count, on=id)
        filename = join(output_folder, "column-%s-analyze.xlsx" % id)
        df_analyze.to_excel(filename, index=False)

    def _analyze_first_token(self, df, id, output_folder="."):
        filename = join(output_folder, "column-%s-analyze.xlsx" % id)
        df_analyze = df[id].value_counts().reset_index(name="count")
        df_analyze = df_analyze.rename({"index": "0"})
        df_analyze.to_excel(filename, index=False)

    def analyze(self, output_folder="."):
        tokens = [token for sublist in self.sentences for token in sublist]
        df = pd.DataFrame(tokens)
        n = df.shape[1]
        self._analyze_first_token(df, 0, output_folder)
        for i in range(1, n):
            self._analyze_field(df, i, output_folder)