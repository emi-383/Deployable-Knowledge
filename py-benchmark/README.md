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
To test the RAG pipeline against different types of retrieval tests, you can easily swap the active dataset.

1. Open `py-benchmark/data_load.py`.

2. Locate the `DATASET_TYPE` constant near the top of the file and change it to one of the supported options:
   * "scifact" - scientific, technical, or fact verification
   * "hotpotqa" - multihop reasoning
   * "nfcorpus" - TREC-Covid: biomedical terminology
   * "nq" - Natural Questions: simulate real user general queries
   
3. Navigate to the benchmark folder and run the loader script again to download the new dataset and sync the TypeScript compiler:
