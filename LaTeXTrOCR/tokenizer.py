import regex as re
import json

class GPT4Tokenizer():
    def __init__(self):
        self.vocab = {idx : bytes([idx]) for idx in range(256)}
        self.merges = dict()
        self.pattern = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
        self.splitby = re.compile(self.pattern)


    def train(self, text, vocab_size):

        assert vocab_size >= 256

        num_merges = vocab_size - 256

        text_splitted = re.findall(self.splitby, text)

        ids = [list(ch.encode("utf-8")) for ch in text_splitted]

        for i in range(num_merges):
            stats = {}
            for _ in ids:
                self.get_pairs(_, stats)
            pair = max(stats, key=stats.get)
            idx = 256 + i
            ids = [self.merge(chunk_ids, pair, idx) for chunk_ids in ids]
            self.merges[pair] = idx
            self.vocab[idx] = self.vocab[pair[0]] + self.vocab[pair[1]]

    
    def encode(self, text):
        tokens = list(text.encode("utf-8"))
        while len(tokens)>=2:
            bigrams = self.get_pairs(tokens)
            pair = min(bigrams, key = lambda p: bigrams.get(p, float("inf")))
            if pair not in self.merges:
                break
            idx = self.merges[pair]
            tokens = self.merge(tokens, pair, idx)
        return tokens
    

    def decode(self, ids):
        tokens = b"".join(self.vocab[idx] for idx in ids)
        text = tokens.decode("utf-8", errors="replace")
        return text


    def get_pairs(self, ids, counts=None):

        counts = {} if counts is None else counts
        for pair in zip(ids, ids[1:]):
            counts[pair] = counts.get(pair, 0) + 1

        return counts


    def merge(self, ids, pair, idx):
        id = 0
        newids = []
        while id<len(ids):
            if id < len(ids)-1 and ids[id]==pair[0] and ids[id+1]==pair[1]:
                newids.append(idx)
                id += 2
            else:
                newids.append(ids[id])
                id+=1
        return newids


    def save_params(self, vocab_file="vocab.json", merges_file="merges.txt"):
        with open(vocab, "w") as vocabfile:
            json.dump(self.vocab, vocabfile)
        with open(merges, "w") as mergesfile:
            mergesfile.write(self.merges)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='text to train the tokenizer on')
    parser.add_argument('vocab_size', type=int, help='desired vocab size')
    parser.add_argument('--vocab_destin', '-vd', help='.json file to save vocab to. Defaults to vocab.txt')
    parser.add_argument('--merges', '-m', help='.txt to save merges to. Defaults to merges.txt')
    args = parser.parse_args()

