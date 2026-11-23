# CampusAssist – Solution Optimization Report

## 1. Objective

The objective of this optimization phase was to identify and reduce avoidable computation in CampusAssist while preserving the existing retrieval behavior.

## 2. Performance Baseline

The original implementation was benchmarked locally using five representative queries per retrieval model.

| Measurement | TF-IDF | Sentence Transformers |
|---|---:|---:|
| Average warm query time | 0.0003 s | 0.0814 s |
| Minimum warm query time | 0.0003 s | 0.0156 s |
| Maximum warm query time | 0.0004 s | 0.3390 s |
| Initialization time | 0.0141 s | 1.7350 s |

These measurements were collected on a local macOS environment. They are not cloud response-time measurements.

## 3. Identified Bottleneck

The semantic retrieval implementation encoded all document titles on every user query.

Since document titles remain unchanged between searches, repeating this operation was unnecessary.

## 4. Optimization Implemented

A cached title-embedding function was introduced in `app.py` using Streamlit's `st.cache_data`.

The application now:
1. Loads the semantic model through the existing cached model loader.
2. Encodes document titles once for a given title list.
3. Reuses cached title embeddings on subsequent queries.
4. Continues to encode each new query independently.
5. Preserves the existing 50% content similarity and 50% title similarity scoring formula.

No training, fine-tuning, or changes to the existing model artifacts were performed.

## 5. Optimized Performance Results

The benchmark was updated to calculate title embeddings once and reuse them across five queries.

| Measurement | Before | After |
|---|---:|---:|
| Semantic average query time | 0.0814 s | 0.0079 s |
| Semantic minimum query time | 0.0156 s | 0.0066 s |
| Semantic maximum query time | 0.3390 s | 0.0092 s |
| TF-IDF average query time | 0.0003 s | 0.0004 s |

The semantic average query time decreased by approximately 90.3%, representing approximately 10.3 times faster warm-query processing in this local benchmark.

The small TF-IDF timing difference is within the variability expected from short local measurements.

## 6. Regression Validation

After the optimization:

- All 13 automated artifact validation tests passed.
- Python compilation checks passed for `app.py` and the benchmark script.
- Existing retrieval evaluation artifacts remained unchanged.
- The retrieval scoring formula and ranking logic were preserved.

The artifact tests validate project data and saved model outputs. They do not independently prove that every Streamlit UI workflow is functioning.

## 7. Remaining Optimization Opportunities

1. Add a validated abstention mechanism for unsupported questions.
2. Expand the evaluation corpus beyond 12 synthetic documents.
3. Evaluate retrieval quality on paraphrased and ambiguous questions.
4. Measure end-to-end response time on the deployed Streamlit application.
5. Conduct user testing to identify interface and usability improvements.
6. Consider caching additional expensive operations if future profiling identifies them as bottlenecks.

## 8. Limitations

- The benchmark contains five representative queries per model.
- Results are local, warm-query measurements.
- Model initialization is reported separately from query latency.
- Streamlit Cloud performance may differ because of hardware, network, cold starts, and runtime conditions.
- The current application does not reliably abstain on unsupported questions.
- No formal load test or production-scale stress test was performed.

## 9. Conclusion

Caching semantic title embeddings addressed an identifiable repeated-computation bottleneck. The local benchmark showed a reduction in average semantic query time from 81.4 ms to 7.9 ms, while all 13 existing automated validation tests continued to pass.

Further work is needed to validate performance in the deployed environment and improve handling of unsupported questions before considering production use.
