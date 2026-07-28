# BEIR Benchmark Suite
This folder and 2 files at root contain the benchmarking infrastructure for the pipeline using BEIR (Benchmarking Information Retrieval) framework.  
Root files: `benchmark_seed.ts`, `benchmark_prep.ts`

## Python
Unlike most of the code for the RAG pipeline, all files in this folder are in Python to natively support the BEIR framework, which is built on Python ecosystem.

## Setup:
Do in order of steps, but redo some sections (and the sections after) as needed when modifying models/components. This suite can run without explicitly running the RAG pipeline first.

###  Run only 1st time
```bash
npm install
npm run db:generate
npm run db:migrate # to be run if there were upstream database changes
cd py-benchmark 
python -m venv .venv

source .venv/bin/activate  # macOS/Linux

.\.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Run each time BEIR dataset is changed
```bash
python data_load.py
cd ..
npm run benchmark-seed
```

### Run each time pipeline is changed
```bash
npm run benchmark-prep
cd py-benchmark
python evaluate.py
cd ..
```

## Switching Datasets
To test the pipeline against different types of BEIR retrieval tests, you can easily swap the active dataset.

1. Open `py-benchmark/data_load.py`.

2. Find the `DATASET_TYPE` constant near the top of the file and change it to some different options:
   * "msmarco"    - general/web search; Bing queries
   * "nq"         - general/web search; Google queries and Wikipedia corpus
   * "trec-covid" - biomedical; covid-19 articles
   * "nfcorpus"   - biomedical; PubMed articles
   * "scifact"    - general scientific and fact checking; PubMed articles
   * "hotpotqa"   - multihop/complex reasoning and fact checking; Wikipedia
   * "fever"      - fact checking; Wikipedia
   * "quora"      - duplicate question pairs
   * "dbpedia-entity" - entity retrieval; DBPedia
   * "arguana"    - argument retrieval

(Can use more than what is listed above. If download url does not exist, comment out `load_dataset(script_dir)` in main of data_load.py. Download separately and ensure dataset is added to `py-benchmark\data` folder and unzipped, and contents inside the dataset folder are `qrels` folder, and `corpus.jsonl` and `queries.jsonl` files.)

3. Navigate to `py-benchmark` folder and run `data_load.py` again.
