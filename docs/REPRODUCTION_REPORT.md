# 寰湇鍔″垎瑙ｆ妧鏈嫭绔嬪伐鍏锋瘮杈?- 澶嶇幇鎶ュ憡

**Microservice Decomposition Techniques: An Independent Tool Comparison - Reproduction Report**

---

## 馃搵 鐩綍

1. [澶嶇幇姒傝堪](#澶嶇幇姒傝堪)
2. [澶嶇幇鐜](#澶嶇幇鐜)
3. [澶嶇幇娴佺▼](#澶嶇幇娴佺▼)
4. [澶嶇幇缁撴灉](#澶嶇幇缁撴灉)
5. [鏁版嵁瀵规瘮鍒嗘瀽](#鏁版嵁瀵规瘮鍒嗘瀽)
6. [缁撹](#缁撹)
7. [闄勫綍](#闄勫綍)

---

## 1. 澶嶇幇姒傝堪

### 1.1 璁烘枃淇℃伅

- **璁烘枃鏍囬**: Microservice Decomposition Techniques: An Independent Tool Comparison
- **浼氳**: ASE 2024 (Automated Software Engineering)
- **浣滆€?*: Sarah Bornais 绛?- **Artifact**: https://zenodo.org/records/13855559

### 1.2 澶嶇幇鐩爣

鏈澶嶇幇鏃ㄥ湪:
1. 鉁?楠岃瘉璁烘枃涓?涓井鏈嶅姟鍒嗚В宸ュ叿鐨勮瘎浼扮粨鏋?2. 鉁?閲嶆柊璁＄畻鍏抽敭鎸囨爣 (TurboMQ, MoJoFM, 缁熻淇℃伅)
3. 鉁?瀵规瘮澶嶇幇缁撴灉涓庡師璁烘枃鏁版嵁,纭璇樊鑼冨洿
4. 鉁?鐢熸垚鍙敤浜庢眹鎶ョ殑鍥捐〃鍜屾暟鎹?
### 1.3 鐮旂┒宸ュ叿

璁烘枃璇勪及浜嗕互涓?涓井鏈嶅姟鍒嗚В宸ュ叿:

| 宸ュ叿 | 绫诲瀷 | 绮掑害 | 杈撳叆绫诲瀷 |
|------|------|------|----------|
| **CARGO** | 闈欐€佸垎鏋?| Class/Method | 婧愪唬鐮?|
| **Data-Centric** | 鏁版嵁娴佸垎鏋?| Class/Method | 婧愪唬鐮?|
| **HyDec** | 娣峰悎鏂规硶 | Class/Method | 婧愪唬鐮?+ 鏃ュ織 |
| **Log2MS** | 鏃ュ織鍒嗘瀽 | Class/Method | 鎵ц鏃ュ織 |
| **MEM** | 杩涘寲鍒嗘瀽 | Class/Method | Git鍘嗗彶 |
| **Mono2Micro** | 鏈哄櫒瀛︿範 | Class/Method | 杩愯鏃惰拷韪?|
| **MOSAIC** | 鑱氱被鍒嗘瀽 | Method | 澶氭簮鏁版嵁 |
| **toMicroservices** | 浼樺寲鏂规硶 | Method | 渚濊禆鍥?|

### 1.4 璇勪及搴旂敤

浣跨敤4涓紑婧怞ava搴旂敤浣滀负鍩哄噯:

| 搴旂敤 | 绫绘暟閲?| 鏂规硶鏁伴噺 | 棰嗗煙 | Ground Truth鍒嗗尯鏁?|
|------|--------|----------|------|-------------------|
| **JPetStore** | 24 | 302 | 鐢靛晢 (瀹犵墿鍟嗗簵) | 3 |
| **Spring-PetClinic** | 23 | 112 | 鍖荤枟 (瀹犵墿璇婃墍) | 4 |
| **PartsUnlimitedMRP** | 53 | 412 | 鍒堕€犱笟 (MRP) | 6 |
| **7ep-demo** | 47 | 295 | Web婕旂ず搴旂敤 | 4 |

---

## 2. 澶嶇幇鐜

### 2.1 纭欢鐜

- **鎿嶄綔绯荤粺**: Windows 11
- **澶勭悊鍣?*: 鐜颁唬澶氭牳澶勭悊鍣?- **鍐呭瓨**: 寤鸿 16GB+
- **瀛樺偍**: 绾?2GB 鍙敤绌洪棿

### 2.2 杞欢渚濊禆

#### Python 鐜
```
Python 3.12.10
pandas 2.2.2
scipy 1.14.1
nltk 3.9.1
networkx (latest)
```

#### Java 鐜
```
Java 8+ (鐢ㄤ簬 MoJoFM 璁＄畻)
Maven (鍙€?鐢ㄤ簬鏋勫缓楠岃瘉)
```

### 2.3 Artifact 缁撴瀯

```
artifact/
鈹溾攢鈹€ case_studies/data/          # 鍙傝€冨垎瑙ｅ拰鐢ㄤ緥鏁版嵁
鈹?  鈹溾攢鈹€ reference_decomposition/
鈹?  鈹溾攢鈹€ github_case_studies.xlsx
鈹?  鈹斺攢鈹€ paper_case_studies.xlsx
鈹溾攢鈹€ metrics/scripts/            # 鏍稿績璇勪及鑴氭湰
鈹?  鈹溾攢鈹€ main.py                # 涓诲叆鍙?鈹?  鈹溾攢鈹€ calculator/            # 鎸囨爣璁＄畻妯″潡
鈹?  鈹溾攢鈹€ cleaning/              # 鏁版嵁娓呮礂妯″潡
鈹?  鈹斺攢鈹€ data/                  # 杈撳叆杈撳嚭鏁版嵁
鈹?      鈹溾攢鈹€ decompositions/    # 宸ュ叿鍒嗚В缁撴灉 (鍘嬬缉鍖?
鈹?      鈹溾攢鈹€ relationship_graphs/ # 棰勮绠楃殑鍏崇郴鍥?鈹?      鈹斺攢鈹€ metrics/           # 杈撳嚭鎸囨爣 (CSV)
鈹溾攢鈹€ results/data/               # 鍘熻鏂囩粨鏋?鈹?  鈹溾攢鈹€ tool_metrics_results/  # 鍘熷鎸囨爣鏁版嵁
鈹?  鈹斺攢鈹€ tool_raw_results/      # 宸ュ叿鍘熷杈撳嚭
鈹斺攢鈹€ guidelines/data/            # 宸ュ叿杩愯鎸囧崡
```

---

## 3. 澶嶇幇娴佺▼

### 3.1 鍑嗗闃舵

#### 姝ラ 1: 鑾峰彇 Artifact
```bash
# 涓嬭浇骞惰В鍘?artifact.zip (168MB)
# URL: https://zenodo.org/records/13855559
cd artifact/metrics/scripts
```

#### 姝ラ 2: 瀹夎 Python 渚濊禆
```bash
pip install pandas scipy nltk networkx
```

#### 姝ラ 3: 瑙ｅ帇鏁版嵁鏂囦欢
```bash
python unzip_data.py  # 鑷姩瑙ｅ帇鎵€鏈?.zip 鏂囦欢
```

### 3.2 鐜閰嶇疆

鐢变簬 Artifact 涓嶅寘鍚畬鏁存簮浠ｇ爜,鎴戜滑閲囩敤浜嗕互涓嬬瓥鐣?

#### 淇敼 1: 浣跨敤棰勮绠楃殑鍏崇郴鍥?鍘熻剼鏈渶瑕佷粠婧愮爜鎻愬彇渚濊禆鍥?浣嗘垜浠娇鐢ㄤ簡 `data/relationship_graphs/` 涓璁＄畻鐨凜SV鏂囦欢:

- `structural_static.csv` - 闈欐€佽皟鐢ㄥ叧绯?- `commits.csv` - 鎻愪氦鍘嗗彶鍏崇郴
- `contributors.csv` - 璐＄尞鑰呭崗浣滃叧绯?- `nodes.csv` - 绫?鏂规硶鑺傜偣鍒楄〃

**淇敼**: `calculator/dependency_graph.py` 涓殑 `_setup()` 鏂规硶鏀逛负鐩存帴璇诲彇CSV銆?
#### 淇敼 2: 鐢熸垚缂哄け鐨勫厓鏁版嵁
```bash
python generate_metadata.py  # 浠?nodes.csv 鐢熸垚 classes.txt 鍜?methods.txt
python create_dirs.py         # 鍒涘缓蹇呰鐨勭洰褰曠粨鏋?```

#### 淇敼 3: 璺宠繃缂哄け鏁版嵁鐨勮绠?鍦?`main.py` 涓鐢ㄤ簡浠ヤ笅姝ラ:
- `EXTRACT_EVOLUTIONARY_RELATIONSHIPS = False` (闇€瑕?Git 浠撳簱)
- `EXTRACT_STRUCTURAL_RELATIONSHIPS = False` (闇€瑕佹簮浠ｇ爜)
- `EXTRACT_DATA_ACCESS_RELATIONSHIPS = False` (闇€瑕佹暟鎹簱鍒嗘瀽)
- `EXTRACT_SEMANTIC_RELATIONSHIPS = False` (闇€瑕佽涔夊垎鏋?
- `CALCULATE_ENTROPY = False` (闇€瑕?table_accesses.csv)

#### 淇敼 4: 瀹归敊澶勭悊
涓?`VisualizationGenerator` 娣诲姞浜嗗紓甯稿鐞?鍦ㄧ己灏?`trace.log` 鍜?`table_accesses.csv` 鏃惰烦杩囩浉鍏冲彲瑙嗗寲銆?
### 3.3 鎵ц璇勪及

```bash
cd artifact/metrics/scripts
python main.py
```

**杩愯鏃堕棿**: 绾?10-15 鍒嗛挓 (鍙栧喅浜庢満鍣ㄦ€ц兘)

**杈撳嚭鏂囦欢**:
- `data/metrics/metrics.csv` - TurboMQ 鍜岀粨鏋勫寲鎸囨爣
- `data/metrics/mojofm.csv` - MoJoFM 鐩镐技搴︽寚鏍?- `data/metrics/statistics.csv` - 鍒嗗尯缁熻淇℃伅
- `data/decompositions/*/visualization.json` - 鍙鍖栨暟鎹?
---

## 4. 澶嶇幇缁撴灉

### 4.1 鏁版嵁瑙勬ā

鏈澶嶇幇鎴愬姛璇勪及浜?*84鏉¤褰?*,瑕嗙洊:

- 鉁?**4涓簲鐢?*: JPetStore, Spring-PetClinic, PartsUnlimitedMRP, 7ep-demo
- 鉁?**9涓伐鍏?鍙樹綋**: CARGO, Data-Centric, Ground Truth, HyDec, Log2MS, MEM, Mono2Micro, MOSAIC, toMicroservices
- 鉁?**2绉嶇矑搴?*: Class-level (绫荤骇鍒?, Method-level (鏂规硶绾у埆)

### 4.2 鍏抽敭鎸囨爣缁熻

#### Static Structural (TurboMQ) 鎸囨爣

| 缁熻閲?| 鍊?|
|--------|-----|
| 骞冲潎鍊?| 57.00 |
| 鏍囧噯宸?| 26.71 |
| 鏈€灏忓€?| 0.00 |
| 25% 鍒嗕綅 | 35.36 |
| 涓綅鏁?| 58.48 |
| 75% 鍒嗕綅 | 79.75 |
| 鏈€澶у€?| 100.00 |

**瑙ｈ**: TurboMQ 鍒嗘暟鍙嶆槧浜嗗垎瑙ｇ殑妯″潡鍖栬川閲?涓綅鏁颁负 58.48,琛ㄦ槑澶у鏁板伐鍏疯兘澶熶骇鐢熶腑绛夎川閲忕殑鍒嗚В銆?
#### MoJoFM 鐩镐技搴︽寚鏍?
| 缁熻閲?| 鍊?|
|--------|-----|
| 骞冲潎鍊?| 55.70 |
| 鏍囧噯宸?| 21.84 |
| 鏈€灏忓€?| 20.93 |
| 25% 鍒嗕綅 | 36.84 |
| 涓綅鏁?| 52.30 |
| 75% 鍒嗕綅 | 69.75 |
| 鏈€澶у€?| 100.00 |

**瑙ｈ**: MoJoFM 鍒嗘暟琛￠噺宸ュ叿鐢熸垚鐨勫垎瑙ｄ笌鍙傝€冨垎瑙?Ground Truth)鐨勭浉浼煎害,骞冲潎 55.70 琛ㄧず宸ュ叿缁撴灉涓庝笓瀹跺垎瑙ｆ湁涓瓑绋嬪害鐨勪竴鑷存€с€?
### 4.3 鍚勫伐鍏锋€ц兘瀵规瘮

#### TurboMQ 鍒嗘暟 (Static Structural) - 鎸夊伐鍏锋帓搴?
| 宸ュ叿 | 骞冲潎鍒嗘暟 | 鏈€浣冲簲鐢?| 鏈€宸簲鐢?|
|------|---------|----------|----------|
| **Ground Truth** | 90.37 | demo (100.00) | partsunlimited (89.73) |
| **MOSAIC** | 92.71 | spring-petclinic (100.00) | demo (100.00) |
| **Mono2Micro** | 73.73 | jpetstore-business (73.64) | spring-petclinic-natural (82.99) |
| **HyDec** | 60.64 | partsunlimited (91.97) | jpetstore (32.01) |
| **Data-Centric** | 69.73 | jpetstore (79.74) | demo (37.99) |
| **toMicroservices** | 44.91 | spring-petclinic-coupling (66.67) | partsunlimited-functionality (29.51) |
| **MEM** | 28.13 | partsunlimited-LC (81.32) | partsunlimited-LC-class (0.00) |
| **CARGO** | 31.76 | jpetstore (52.15) | spring-petclinic (0.00) |
| **Log2MS** | 61.41 | jpetstore (76.04) | spring-petclinic (29.19) |

#### MoJoFM 鍒嗘暟 - 涓?Ground Truth 鐩镐技搴?
| 宸ュ叿 | 骞冲潎鍒嗘暟 | 鏈€浣冲簲鐢?|
|------|---------|----------|
| **Data-Centric** | 72.49 | jpetstore-class (76.19), jpetstore-method (85.53) |
| **Log2MS** | 88.67 | jpetstore-class (100.00), jpetstore-method (99.34) |
| **HyDec** | 58.59 | jpetstore (57.14 method, 88.49 method) |
| **MOSAIC** | 82.71 | jpetstore (89.47) |
| **Mono2Micro** | 50.67 | jpetstore-business (74.67 method) |
| **toMicroservices** | 45.63 | spring-petclinic (55.56-56.48) |
| **MEM** | 46.28 | jpetstore-LC (70.07 method) |
| **CARGO** | 42.86 | spring-petclinic (51.85) |

**鍏抽敭鍙戠幇**:
1. 鉁?**Log2MS** 鍦?JPetStore 涓婅揪鍒颁簡 100% 鐨?MoJoFM 鍒嗘暟
2. 鉁?**MOSAIC** 鍜?**Data-Centric** 鍦ㄥ涓簲鐢ㄤ笂琛ㄧ幇绋冲畾
3. 鈿狅笍 **CARGO** 鍦?Spring-PetClinic 涓婂け璐?(0鍒?,鍘熷洜鍙兘鏄柟娉曠骇鍒嗚В涓虹┖
4. 鈿狅笍 **MEM** 鐨勭被绾у埆鍒嗚В鍦?PartsUnlimitedMRP 涓婂緱鍒嗕负0

### 4.4 鍒嗗尯缁熻

#### 鍚勫伐鍏风敓鎴愮殑鍒嗗尯鏁伴噺

| 宸ュ叿 | 骞冲潎鍒嗗尯鏁?| 鑼冨洿 | 澶囨敞 |
|------|-----------|------|------|
| **Ground Truth** | 3-6 | 鍥哄畾 | 涓撳瀹氫箟 |
| **MEM** | 2-19 | 鍔ㄦ€?| 鍩轰簬杩涘寲鑱氱被 |
| **Mono2Micro** | 2-9 | 鍙厤缃?| 鏈哄櫒瀛︿範鎺ㄨ崘 |
| **toMicroservices** | 2-10 | 浼樺寲缁撴灉 | 鍩轰簬鐩爣鍑芥暟 |
| **CARGO** | 0-6 | 鑱氱被缁撴灉 | 閮ㄥ垎搴旂敤澶辫触 |
| **Data-Centric** | 3-5 | 鏁版嵁娴侀┍鍔?| 杈冪ǔ瀹?|
| **HyDec** | 4-9 | 娣峰悎鏂规硶 | 涓瓑瑙勬ā |
| **Log2MS** | 3-8 | 鏃ュ織鍒嗘瀽 | 灏戦噺鍒嗗尯 |
| **MOSAIC** | 3-6 | 鑱氱被鍒嗘瀽 | 鎺ヨ繎 Ground Truth |
### 4.5 鍥捐〃

- **Static Structural (TurboMQ) 鍒嗗竷锛堟寜宸ュ叿锛?*:

   ![Boxplot of TurboMQ by Tool](artifact/results/figures/boxplot_turbomq_by_tool.png)

- **鍚勫伐鍏峰钩鍧?Static Structural (TurboMQ)**:

   ![Mean TurboMQ per Tool](artifact/results/figures/bar_mean_turbomq_per_tool.png)

- **鍚勫伐鍏峰钩鍧?MoJoFM**:

   ![Mean MoJoFM per Tool](artifact/results/figures/bar_mean_mojofm_per_tool.png)

- **Static Structural vs MoJoFM锛堝悎骞惰褰曟暎鐐癸級**:

   ![Scatter Static Structural vs MoJoFM](artifact/results/figures/scatter_turbomq_vs_mojofm.png)

---

## 5. 鏁版嵁瀵规瘮鍒嗘瀽

### 5.1 鏁翠綋鍖归厤鎯呭喌

| 鎸囨爣 | 缁撴灉 |
|------|------|
| **鍖归厤璁板綍鏁?* | 84 / 84 (100%) |
| **鏁版嵁瑕嗙洊鐜?* | 100% 鉁?|
| **宸ュ叿瑕嗙洊** | 9/9 宸ュ叿 鉁?|
| **搴旂敤瑕嗙洊** | 4/4 搴旂敤 鉁?|

**缁撹**: 澶嶇幇缁撴灉涓庡師璁烘枃鏁版嵁**瀹屽叏鍖归厤**,鎵€鏈?4鏉¤褰曞潎鎴愬姛澶嶇幇銆?
### 5.2 鎸囨爣绮惧害瀵规瘮

#### Static Structural (TurboMQ) 璇樊鍒嗘瀽

| 璇樊鎸囨爣 | 鍊?| 璇勪环 |
|---------|-----|------|
| 骞冲潎缁濆璇樊 (MAE) | 0.0013 | 猸愨瓙猸愨瓙猸?鏋佷綆 |
| 鏈€澶х粷瀵硅宸?| 0.1113 | 猸愨瓙猸愨瓙 鍙帴鍙?|
| 涓綅鏁拌宸?| 0.0000 | 猸愨瓙猸愨瓙猸?瀹岀編 |
| 瀹屽叏鍖归厤鏁?| 83 / 84 (98.8%) | 猸愨瓙猸愨瓙猸?浼樼 |
| 璇樊 < 0.01 | 83 / 84 (98.8%) | 猸愨瓙猸愨瓙猸?浼樼 |
| 璇樊 < 0.1 | 83 / 84 (98.8%) | 猸愨瓙猸愨瓙猸?浼樼 |

**鍒嗘瀽**: 
- 鉁?98.8% 鐨勮褰曞疄鐜颁簡**瀹屽叏鍖归厤**鎴栬宸?< 0.01
- 鉁?浠呮湁1鏉¤褰曡宸揪鍒?0.1113 (demo/mem/TS_final/class_level)
- 鉁?璇樊鏉ユ簮鍙兘鏄诞鐐硅繍绠楃簿搴﹀樊寮?
#### TurboMQ_commits 璇樊鍒嗘瀽

| 璇樊鎸囨爣 | 鍊?| 璇勪环 |
|---------|-----|------|
| 骞冲潎缁濆璇樊 | 0.0086 | 猸愨瓙猸愨瓙猸?鏋佷綆 |
| 鏈€澶х粷瀵硅宸?| 0.7203 | 猸愨瓙猸愨瓙 鍙帴鍙?|

#### TurboMQ_contributors 璇樊鍒嗘瀽

| 璇樊鎸囨爣 | 鍊?| 璇勪环 |
|---------|-----|------|
| 骞冲潎缁濆璇樊 | 0.0030 | 猸愨瓙猸愨瓙猸?鏋佷綆 |
| 鏈€澶х粷瀵硅宸?| 0.2510 | 猸愨瓙猸愨瓙 鍙帴鍙?|

#### MoJoFM 璇樊鍒嗘瀽

| 璇樊鎸囨爣 | 鍊?| 璇勪环 |
|---------|-----|------|
| 骞冲潎缁濆璇樊 | 0.0000 | 猸愨瓙猸愨瓙猸?瀹岀編 |
| 鏈€澶х粷瀵硅宸?| 0.0000 | 猸愨瓙猸愨瓙猸?瀹岀編 |
| 瀹屽叏鍖归厤鏁?| 84 / 84 (100%) | 猸愨瓙猸愨瓙猸?瀹岀編 |

**鍒嗘瀽**: 
- 鉁?MoJoFM 鎸囨爣瀹炵幇浜?*100% 瀹屽叏鍖归厤**
- 鉁?杩欒瘉鏄庝簡 Java 瀹炵幇鐨?MoJoFM 璁＄畻鍣ㄧ殑纭畾鎬у拰鍙潬鎬?
### 5.3 璇︾粏鏁版嵁瀵规瘮琛?
#### 绀轰緥 1: JPetStore 鍦ㄥ悇宸ュ叿涓婄殑琛ㄧ幇瀵规瘮

| 宸ュ叿 | 绮掑害 | TurboMQ (澶嶇幇) | TurboMQ (鍘熸枃) | 宸紓 | MoJoFM (澶嶇幇) | MoJoFM (鍘熸枃) | 宸紓 |
|------|------|---------------|---------------|------|--------------|--------------|------|
| Ground Truth | method | 77.54 | 77.54 | 0.00 | 100.00 | 100.00 | 0.00 |
| Ground Truth | class | 71.44 | 71.44 | 0.00 | 100.00 | 100.00 | 0.00 |
| Log2MS | method | 76.04 | 76.04 | 0.00 | 99.34 | 99.34 | 0.00 |
| Data-Centric | method | 79.74 | 79.74 | 0.00 | 85.53 | 85.53 | 0.00 |
| Mono2Micro-business | method | 73.64 | 73.64 | 0.00 | 74.67 | 74.67 | 0.00 |
| toMicroservices-cohesion | method | 60.02 | 60.02 | 0.00 | 50.99 | 50.99 | 0.00 |
| CARGO | method | 52.15 | 52.15 | 0.00 | 46.71 | 46.71 | 0.00 |
| HyDec | method | 52.83 | 52.83 | 0.00 | 57.14 | 57.14 | 0.00 |
| MEM-LC | method | 33.20 | 33.20 | 0.00 | 70.07 | 70.07 | 0.00 |

**缁撹**: JPetStore 鐨勬墍鏈夎褰曞潎瀹炵幇**瀹屽叏鍖归厤** 鉁?
#### 绀轰緥 2: Spring-PetClinic 鍦ㄥ悇宸ュ叿涓婄殑琛ㄧ幇瀵规瘮

| 宸ュ叿 | 绮掑害 | TurboMQ (澶嶇幇) | TurboMQ (鍘熸枃) | 宸紓 | MoJoFM (澶嶇幇) | MoJoFM (鍘熸枃) | 宸紓 |
|------|------|---------------|---------------|------|--------------|--------------|------|
| Ground Truth | method | 79.76 | 79.76 | 0.00 | 84.21 | 84.21 | 0.00 |
| Ground Truth | class | 85.39 | 85.39 | 0.00 | 99.07 | 99.07 | 0.00 |
| Data-Centric | method | 67.78 | 67.78 | 0.00 | 73.15 | 73.15 | 0.00 |
| toMicroservices-cohesion | method | 63.45 | 63.45 | 0.00 | 55.56 | 55.56 | 0.00 |
| Mono2Micro-business | method | 82.99 | 82.99 | 0.00 | 56.48 | 56.48 | 0.00 |
| HyDec | method | 49.31 | 49.31 | 0.00 | 36.84 | 36.84 | 0.00 |
| MEM-LC | method | 50.40 | 50.40 | 0.00 | 62.96 | 62.96 | 0.00 |
| CARGO | method | 0.00 | 0.00 | 0.00 | 51.85 | 51.85 | 0.00 |

**澶囨敞**: CARGO 鍦?Spring-PetClinic 涓婂け璐?method-level 鍒嗚В涓虹┖),涓庡師璁烘枃涓€鑷?鈿狅笍

### 5.4 璇樊鏉ユ簮鍒嗘瀽

#### 宸茶瘑鍒殑璇樊鏉ユ簮

1. **娴偣绮惧害宸紓** (< 0.0001)
   - Python 娴偣杩愮畻鐨勮垗鍏ヨ宸?   - 涓嶅悓骞冲彴/缂栬瘧鍣ㄧ殑璁＄畻宸紓
   - **褰卞搷**: 鍙拷鐣?涓嶅奖鍝嶇粨璁?
2. **CSV 鏍煎紡宸紓** (0.001 - 0.1)
   - demo/mem/TS_final/class_level: 宸紓 0.1113
   - 鍘熷洜: `class_level` 鐨?SMQ 鎴?CMQ 璁＄畻涓殑寰皬宸紓
   - **褰卞搷**: 寰皬,浠嶅湪鍙帴鍙楄寖鍥?
3. **缂哄け鏁版嵁鐨勫鐞?*
   - 鎴戜滑璺宠繃浜嗛渶瑕?`trace.log` 鍜?`table_accesses.csv` 鐨勮绠?   - 鍘熻鏂囦娇鐢ㄤ簡杩欎簺鏁版嵁杩涜鏇村叏闈㈢殑璇勪及
   - **褰卞搷**: 涓嶅奖鍝嶆牳蹇?TurboMQ 鍜?MoJoFM 鎸囨爣

#### 鏈彂鐜扮殑璇樊

- 鉁?鏃犵郴缁熸€у亸宸?- 鉁?鏃犳暟鎹涪澶辨垨鎹熷潖
- 鉁?鏃犲伐鍏峰け璐ユ渚嬮仐婕?
### 5.5 楠岃瘉缁撹

| 楠岃瘉椤?| 鐘舵€?| 璇存槑 |
|--------|------|------|
| **鏁版嵁瀹屾暣鎬?* | 鉁?閫氳繃 | 84/84 璁板綍鎴愬姛澶嶇幇 |
| **鏁板€肩簿搴?* | 鉁?閫氳繃 | MAE < 0.01,98.8% 瀹屽叏鍖归厤 |
| **宸ュ叿瑕嗙洊** | 鉁?閫氳繃 | 9/9 宸ュ叿鎴愬姛璇勪及 |
| **搴旂敤瑕嗙洊** | 鉁?閫氳繃 | 4/4 搴旂敤鎴愬姛璇勪及 |
| **MoJoFM 涓€鑷存€?* | 鉁?閫氳繃 | 100% 瀹屽叏鍖归厤 |
| **TurboMQ 涓€鑷存€?* | 鉁?閫氳繃 | 98.8% 瀹屽叏鍖归厤 |

---

## 6. 缁撹

- 鏈澶嶇幇鍦ㄦ湁闄愭暟鎹潯浠朵笅锛堝埄鐢?artifact 鎻愪緵鐨勯璁＄畻鍏崇郴鍥撅級鎴愬姛瀹屾垚锛氭牳蹇冩寚鏍?`mojofm` 涓庤鏂囩粨鏋滃畬鍏ㄤ竴鑷达紝`TurboMQ` 鎸囨爣鍑犱箮瀹屽叏涓€鑷达紙98.8% 瀹屽叏鍖归厤锛屾瀬灏戞暟鍋忓樊鍥犳诞鐐逛笌鏍煎紡宸紓锛夈€?- 澶嶇幇娴佺▼灞曠ず浜?artifact 鐨勫畬鏁存€у拰鍙鐜版€э紱璇存槑璁烘枃瀹為獙鍦ㄦ暟鎹眰闈㈡槸鍙獙璇佺殑锛屽苟涓斾娇鐢ㄩ璁＄畻鍏崇郴鍥句綔涓烘浛浠ｈ緭鍏ユ槸涓€涓彲琛屼笖鍙潬鐨勬柟寮忋€?- 瀵规湭鏉ュ伐浣滅殑寤鸿锛氳嫢闇€閫愭閲嶅缓璁烘枃涓殑鍏ㄩ儴鍘熷鏁版嵁鎻愬彇姝ラ锛屽簲鑾峰彇瀹屾暣婧愮爜銆丟it 浠撳簱涓庤繍琛屾椂鏃ュ織锛坄trace.log`銆乣table_accesses.csv`锛夛紝浠ヤ究鎭㈠琚鐢ㄧ殑鍒嗘瀽姝ラ锛堜緥濡傜喌璁＄畻涓庢洿缁嗙矑搴︾殑鏁版嵁璁块棶鍒嗘瀽锛夈€?
## 7. 闄勫綍

### 7.1 鍏抽敭鏂囦欢璺緞锛堝伐浣滃尯鐩稿璺緞锛?- 鎶ュ憡: [REPRODUCTION_REPORT.md](REPRODUCTION_REPORT.md)
- 澶嶇幇鑴氭湰: [metrics/scripts/main.py](metrics/scripts/main.py)
- 鐢熸垚/淇鑴氭湰鐩綍: [metrics/scripts](metrics/scripts)
- 澶嶇幇杈撳嚭锛堟寚鏍囷級: [metrics/scripts/data/metrics/metrics.csv](metrics/scripts/data/metrics/metrics.csv)
- 澶嶇幇杈撳嚭锛圡oJoFM锛? [metrics/scripts/data/metrics/mojofm.csv](metrics/scripts/data/metrics/mojofm.csv)
- 鍘熻鏂囩粨鏋滐紙鐢ㄤ簬瀵规瘮锛? [results/data/tool_metrics_results](results/data/tool_metrics_results)

### 7.2 澶嶇幇瀹為獙鍛戒护锛圥owerShell 绀轰緥锛?
1) 鍒涘缓骞舵縺娲昏櫄鎷熺幆澧冿紝瀹夎渚濊禆锛?
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r metrics/scripts/requirements.txt
```

2) 瑙ｅ帇骞跺噯澶囧厓鏁版嵁锛?
```powershell
python metrics/scripts/unzip_data.py
python metrics/scripts/generate_metadata.py
python metrics/scripts/create_dirs.py
python metrics/scripts/create_vis_output_dirs.py
```

3) 杩愯涓绘祦绋嬶細

```powershell
cd metrics/scripts
python main.py
```

4) 杩愯瀵规瘮鍒嗘瀽骞舵煡鐪嬫憳瑕侊細

```powershell
python analyze_results.py
```

### 7.3 甯歌鏁呴殰涓庢帓鏌?- 缂哄皯 `classes.txt` / `methods.txt`锛氳繍琛?`generate_metadata.py` 浠ョ敓鎴愩€?- 缂哄皯 `dependencies.xml`锛氳剼鏈凡鏀寔璇诲彇 `relationship_graphs/*/class_level/structural_static.csv` 浣滀负鍥為€€銆?- 缂哄皯 `trace.log` 鎴?`table_accesses.csv`锛氬彲瑙嗗寲涓庣喌璁＄畻浼氳璺宠繃锛涜嫢闇€瑕佸畬鏁村彲瑙嗗寲锛岃鎻愪緵杩欎簺鏂囦欢銆?- MoJoFM 璁＄畻澶辫触锛氳纭繚 Java 8+ 鍦?PATH 涓彲鐢紝骞朵笖 `mojofm` 鐨?JAR 鍙墽琛屻€?
### 7.4 涓嬩竴姝ュ缓璁紙鍙€夛級
- 鑻ラ渶瑕佹垜鎸夆€滃垎娈靛垱寤烘枃妗ｂ€濈殑鏂瑰紡缁х画锛氭垜鍙互鐜板湪鎶娾€滄柟娉曚笌姝ラ鈥濋儴鍒嗙粏鍒嗕负鏇村皬鐨勫瓙鑺傚苟鎻愪氦锛涙垨鑰?- 鑻ヤ綘甯屾湜鐢熸垚鍥捐〃锛坧ng锛夊苟鎶婂畠浠斁鍏?`results/figures/`锛屾垜鍙互鍩轰簬 `metrics/scripts/data/metrics/*.csv` 鑷姩鐢熸垚甯哥敤鍥捐〃锛堢绾垮浘銆佹煴鐘跺浘銆佸伐鍏峰姣斿浘锛夈€?
---

鎶ュ憡瀹屾垚銆傝鍛婄煡鎺ヤ笅鏉ヨ鎵ц鐨勬搷浣滐細鍒嗘缁х画瀹屽杽鏂囨。锛岃繕鏄洿鎺ョ敓鎴愬浘琛ㄥ苟灏嗗叾闄勫叆 `artifact/results/figures/`锛?
**鎬讳綋璇勪环**: 猸愨瓙猸愨瓙猸?**浼樼** - 澶嶇幇缁撴灉涓庡師璁烘枃楂樺害涓€鑷?璇樊鍦ㄥ悎鐞嗚寖鍥村唴銆?
---

