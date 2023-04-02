## Pinyin IME Models


In response to the call for carbon neutrality, probabilistic models are now open source to avoid repetitive computational power consumption in operations.


### Usage
See main.py
```python
from utils import get_prefix_model_value, load_probabilistic_model
probabilistic_model = load_probabilistic_model("trigram_std/probabilistic_model.gz")
    prob = get_prefix_model_value(
        model=probabilistic_model,
        prefix="北京",
        token="是"
    )
    print("p({}|{}) = {}".format("是", "北京", str(prob)))
    # p(是|北京) = 0.25
```

### Details

| model | corpora |
| ---- | ---- |
| bigram | sina |
| bigram_std | std_output.txt |
| bigram_weibo_baike_webtext_wiki | sina weibo baike webtext wiki |
| bigram_weibo_newscrawl_baike_webtext_wiki | sina newscrawl weibo baike webtext wiki |
| trigram | sina |
| trigram_std | std_output.txt |
| trigram_weibo_baike_webtext_wiki | sina weibo baike webtext wiki |
| trigram_weibo_newscrawl_baike_webtext_wiki | sina newscrawl weibo baike webtext wiki |

Please indicate the reference when using

Trigram models can be found here: https://cloud.tsinghua.edu.cn/d/cffa2e2502ed4fd59d1b/

### Baseline
| tester | model | top k | language modeling | time usage | sentence acc | word acc | 
| ------ | ---- | ---- | ---- | ---- | ---- | ---- |
| song on r3 1200 | bigram | 4 | None | 25.88 | 0.399 | 0.842 |
| song on r3 1200 | bigram | 4 | uer/gpt2-chinese-cluecorpussmall | 32.18 | 0.570 | 0.887 |
| song on r3 1200 | bigram_std | 4 | None | 22.48 | 0.970 | 0.997 |
| song on r3 1200 | bigram_weibo_baike_webtext_wiki | 4 | None | 26.72 | 0.421 |  0.848 |
| song on r3 1200 | bigram_weibo_newscrawl_baike_webtext_wiki | 4 | None | 27.02 | 0.451 | 0.861 |
| song on r3 1200 | trigram | 4 | None | 25.34 | 0.637 | 0.909 |
| song on r3 1200 | trigram_std | 4 | None | 22.42 | 1.000 | 1.000 |
| song on r3 1200 | trigram_weibo_baike_webtext_wiki | 4 | None | 26.75 | 0.782 |  0.955 |
| song on r3 1200 | trigram_weibo_newscrawl_baike_webtext_wiki | 4 | None | 26.48 | 0.808 | 0.961 |

To be updated.

For your reference only.

