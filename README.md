```markdown
# task-0

## Requirements
* Python 3+
* pip

## Installation

Clone the repository:
```
git clone [https://github.com/DataPirate3119/take-0.git](https://github.com/DataPirate3119/take-0.git)
cd task-0

```

Install required packages:

```
pip install numpy pandas matplotlib

```

## Usage

Each question is implemented in its respective script file (`q1.py` through `q6.py`). Run them from the project root directory using the commands below:

### 1. List Analyzer (`q1.py`)

Calculates min, max, sum, counts of even and odd integers, and reverses a list.

```
python3 q1.py

```

### 2. List Copying & Methods (`q2.py`)

List mutation using `.copy()` to keep the original dataset unchanged while modifying and sorting a copy.

```
python3 q2.py

```

### 3. Prime Numbers using `for-else` (`q3.py`)

Determines prime numbers from 2 to N using `for-else`.

```
python3 q3.py

```

### 4. NumPy Array Operations (`q4.py`)

Performs vectorized calculations, statistical aggregation (`mean`, `std`), scalar additions, and Boolean masking on array data.

```
python3 q4.py

```

### 5. Pandas Data Processing (`q5.py`)

Loads `student_performance.csv`, checks for missing values, analyzes data, creates calculated columns (`Improvement`), filters records, and outputs `processed_student_performance.csv`.

```
python3 q5.py

```

### 6. Matplotlib Data Visualization (`q6.py`)

Generates visualization plots from the processed CSV and saves PNG outputs into the `plots/` directory:

* `final_scores.png`: Bar chart of student final scores.
* `study_vs_score.png`: Scatter plot comparing hours studied vs. final scores.
* `score_distribution.png`: Histogram showing frequency distribution of final scores.
* `bitsplot.png`: Custom plot highlighting impact of attendance on final scores (none tbh).

```
python3 q6.py

```
