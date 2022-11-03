# 🐠

## Requirements
```bash
pip install pandas tqdm tabulate
```

## Input file format
```
- <name1>
day: start-end, start-end
day: start-end, start-end, start-end
day: start-end
day: start-end
day: start-end
- <name2>
day: start-end
day: start-end
.
.
.
```

For example,
```
- 햄만혁
월: 15-18
화: 15-18
수: 15-18
목: 15-18
금: 15-18
- 힘만햄
화: 11-16
수: 11-16
- 만혁햄
화: 16-19
수: 16-17
목: 16-17
금: 13-15
```
See [`input.txt`](./input.txt).

## Usage
```bash
python main.py <path_to_input_file> -n <num_solutions> -o <output>
```

### Example
```bash
python main.py input.txt -n 3 -o timetable
```
The schedule tables will be stored to `timetable_x.csv`.

```
Scheduling using GA...
100%|█████████████████████████████████████████████████████| 100/100 [00:00<00:00, 134.26it/s]
Done
=================== Option #1 ===================

name    ideal   actual
기미규  0.071   0.077
기지호  0.047   0.046
Justina 0.033   0.031
기혀겨  0.014   0.031
유차우  0.033   0.077
이도후  0.099   0.108
제여서  0.094   0.046
조미우  0.047   0.046
조유지  0.127   0.077
시수요  0.165   0.200
이서주  0.212   0.200
배주규  0.057   0.062

|   start_time | 월     | 화     | 수     | 목     | 금      |
|-------------:|:-------|:-------|:-------|:-------|:--------|
|            8 | 유차우 | 기혀겨 | 기혀겨 | 유차우 | 유차우  |
|            9 | 유차우 | 이서주 | 배주규 | 유차우 | 제여서  |
|           10 | 시수요 | 이서주 | 배주규 | 배주규 | 제여서  |
|           11 | 시수요 | 이서주 | 시수요 | 배주규 | 제여서  |
|           12 | 이서주 | 기지호 | 시수요 | 시수요 | 조유지  |
|           13 | 이서주 | 기지호 | 시수요 | 시수요 | Justina |
|           14 | 이서주 | 기지호 | 시수요 | 이도후 | Justina |
|           15 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           16 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           17 | 이도후 | 이도후 | 기미규 | 시수요 | 조유지  |
|           18 | 이서주 | 시수요 | 조미우 | 시수요 | 조유지  |
|           19 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |
|           20 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |

=================== Option #2 ===================

name    ideal   actual
기미규  0.071   0.077
기지호  0.047   0.046
Justina 0.033   0.031
기혀겨  0.014   0.031
유차우  0.033   0.077
이도후  0.099   0.108
제여서  0.094   0.046
조미우  0.047   0.046
조유지  0.127   0.077
시수요  0.165   0.200
이서주  0.212   0.200
배주규  0.057   0.062

|   start_time | 월     | 화     | 수     | 목     | 금      |
|-------------:|:-------|:-------|:-------|:-------|:--------|
|            8 | 유차우 | 기혀겨 | 기혀겨 | 유차우 | 유차우  |
|            9 | 유차우 | 이서주 | 배주규 | 유차우 | 제여서  |
|           10 | 시수요 | 이서주 | 배주규 | 배주규 | 제여서  |
|           11 | 시수요 | 이서주 | 시수요 | 배주규 | 제여서  |
|           12 | 이서주 | 기지호 | 시수요 | 시수요 | 조유지  |
|           13 | 이서주 | 기지호 | 시수요 | 시수요 | Justina |
|           14 | 이서주 | 기지호 | 시수요 | 이도후 | Justina |
|           15 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           16 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           17 | 이도후 | 이도후 | 기미규 | 시수요 | 조유지  |
|           18 | 이서주 | 시수요 | 조미우 | 시수요 | 조유지  |
|           19 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |
|           20 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |

=================== Option #3 ===================

name    ideal   actual
기미규  0.071   0.077
기지호  0.047   0.046
Justina 0.033   0.031
기혀겨  0.014   0.031
유차우  0.033   0.077
이도후  0.099   0.108
제여서  0.094   0.046
조미우  0.047   0.046
조유지  0.127   0.077
시수요  0.165   0.200
이서주  0.212   0.200
배주규  0.057   0.062

|   start_time | 월     | 화     | 수     | 목     | 금      |
|-------------:|:-------|:-------|:-------|:-------|:--------|
|            8 | 유차우 | 기혀겨 | 기혀겨 | 유차우 | 유차우  |
|            9 | 유차우 | 이서주 | 배주규 | 유차우 | 제여서  |
|           10 | 시수요 | 이서주 | 배주규 | 배주규 | 제여서  |
|           11 | 시수요 | 이서주 | 시수요 | 배주규 | 제여서  |
|           12 | 이서주 | 기지호 | 시수요 | 시수요 | 조유지  |
|           13 | 이서주 | 기지호 | 시수요 | 시수요 | Justina |
|           14 | 이서주 | 기지호 | 시수요 | 이도후 | Justina |
|           15 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           16 | 이도후 | 이도후 | 기미규 | 기미규 | 이서주  |
|           17 | 이도후 | 이도후 | 기미규 | 시수요 | 조유지  |
|           18 | 이서주 | 시수요 | 조미우 | 시수요 | 조유지  |
|           19 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |
|           20 | 이서주 | 조유지 | 조미우 | 시수요 | 이서주  |
```
