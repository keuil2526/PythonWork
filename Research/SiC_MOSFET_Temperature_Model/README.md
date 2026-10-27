# SiC MOSFET Temperature-Dependence Modeling

단일 SCT3080KL SiC MOSFET의 온도별 측정 데이터를 분석하기 위한 Python 프로젝트입니다. 데이터가 준비되면 CSV를 채우고 명령어 한 번으로 문턱전압, 온 저항, 경험적 온도 모델, 그래프 및 결과 파일을 생성할 수 있습니다.

## 분석 범위

- Transfer Curve에서 고정 전류 기준으로 문턱전압 (V_{th}) 추출
- 온도별 (V_{th}) 선형 근사: (V_{th}(T)=V_{th,0}+a(T-T_0))
- 온 저항의 경험적 온도 모델: (R_{DS(on)}(T)=R_0(T/T_0)^m)
- 데이터가 충분할 경우 Transfer Curve의 기울기 (g_m=d|I_D|/dV_{GS})를 이용한 경험적 모델
- CSV 요약, PNG 그래프, JSON 파라미터 결과 저장

## 1. 설치

Python 3.10 이상을 권장합니다.

Linux/Ubuntu:

```bash
cd Research/SiC_MOSFET_Temperature_Model
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. 데이터 입력

`data/temperature_measurements.csv`에 측정 데이터를 입력합니다. 템플릿의 열 이름을 그대로 사용하세요. **한 행은 측정 곡선의 한 측정점**입니다.

| 열 | 필수 여부 | 의미 |
|---|---|---|
| `temperature_C` | 필수 | 측정 온도(°C) |
| `curve_type` | 필수 | `transfer`, `output`, `rds_on` 중 하나 |
| `vgs_V` | 필수 | 게이트-소스 전압(V) |
| `vds_V` | 필수 | 드레인-소스 전압(V) |
| `id_A` | 필수 | 드레인 전류(A) |
| `rds_on_ohm` | 선택 | 장비가 직접 산출한 온 저항(Ω). 없으면 rds_on 행에서 `abs(VDS/ID)`로 계산 |
| `device_id` | 선택 | 소자 식별자. 단일 소자는 예: `SCT3080KL_01` |
| `notes` | 선택 | 측정 조건 및 메모 |

각 온도에서 Transfer Curve를 기록하려면 각 VGS 측정점마다 행을 추가하고 `curve_type=transfer`로 설정합니다. Output Curve도 각 측정점마다 한 행씩 기록합니다. 온 저항 데이터는 `curve_type=rds_on`으로 기록하거나 `rds_on_ohm` 열에 장비 산출값을 넣습니다.

측정 장비가 mA 단위로 전류를 내보낸다면 CSV에 입력하기 전에 A 단위로 변환하세요. 예를 들어 125 mA는 0.125 A입니다. 저항은 Ω 단위로 통일하세요. 온도는 °C로 입력합니다. 프로그램은 모델 피팅에 필요한 곳에서 K로 변환합니다.

Transfer Curve에서 문턱전압 추출에 사용할 고정 전류 기준은 장비/데이터시트의 정의와 연구 프로토콜에 맞춰 지정해야 합니다. 아래 예시의 1 mA는 기본값일 뿐이며, 반드시 실제 측정 조건에 맞는지 확인하세요.

## 3. 실행

프로젝트 폴더에서:

```bash
python analyze_sic_mosfet.py --input data/temperature_measurements.csv --outdir results --threshold-current-a 0.001 --vgs-for-rds 18
```

- `--threshold-current-a`: 문턱전압 추출 기준 전류의 절댓값(A). 측정 기준에 맞게 설정
- `--vgs-for-rds`: 온 저항 분석에 사용할 목표 게이트 전압(V). 해당 전압 부근의 데이터만 사용
- `--vgs-tolerance`: 목표 VGS 허용 오차(V), 기본 0.5 V
- `--t0-c`: 기준 온도(°C), 기본 25°C

예를 들어 측정 기준 전류가 250 µA라면 `--threshold-current-a 0.00025`로 실행합니다. 기준 전류는 임의로 정하지 말고 데이터시트 또는 연구에서 정한 기준을 사용하세요.

## 4. 결과물

실행 후 `results/`에 다음 결과가 생성됩니다.

- `cleaned_measurements.csv`: 기본 정리 데이터
- `vth_by_temperature.csv`: 온도별 문턱전압 추출값
- `rds_on_by_temperature.csv`: 온도별 온 저항 요약값
- `fit_results.json`: 모델 파라미터와 적합도
- `vth_vs_temperature.png`: 문턱전압 그래프
- `rds_on_vs_temperature.png`: 온 저항 그래프
- `transfer_curves.png`: Transfer Curve
- `output_curves.png`: Output Curve
- `gm_empirical_model.png`: 데이터가 충분할 때 경험적 gm 모델 그래프

## 5. 모델 해석 시 주의사항

1. (V_{th}) 추출값은 고정 전류 기준에 의존합니다. 모든 온도에서 같은 기준과 측정 절차를 사용하세요.
2. (R_{DS(on)})는 VGS, ID, VDS, 펄스/연속 측정, 열적 안정화 등 측정 조건에 영향을 받습니다. 조건이 다른 데이터를 무심코 합치지 마세요.
3. (R_{DS(on)}=R_0(T/T_0)^m)은 경험적 근사입니다. (m)을 특정 산란 기작의 직접적인 증거로 해석하지 마세요.
4. 프로그램의 gm 기반 모델은 **유효 트랜스컨덕턴스의 경험적 모델**입니다. 소자 형상(W/L), 산화막 정전용량(Cox), 채널 저항의 신뢰할 수 있는 분리 없이 절대 이동도 (mu_{eff})를 직접 산출했다고 주장하지 마세요.
5. (	heta)와 온도 지수는 데이터 범위 및 모델 가정에 의존합니다. 적합도와 함께 잔차, 측정 조건 및 파라미터 식별 가능성을 검토하세요.
6. 소자 하나의 결과는 해당 소자에 대한 사례 분석입니다. 모든 SCT3080KL 또는 모든 Planar/Trench MOSFET에 일반화하지 마세요.
7. 코드가 생성한 모델/그래프는 측정 데이터에 기반합니다. 템플릿만으로는 과학적 결과가 만들어지지 않습니다.

## 6. 권장 측정 조건 기록

각 데이터 파일과 별도 실험 기록에 다음을 남기세요: 실제 소자 식별자, 온도 센서 위치, 열적 안정화 시간, VGS/VDS 스윕 범위, 전류 컴플라이언스, 펄스/연속 측정 여부, 측정 순서, 장비 모델 및 교정 상태.

## License

연구 및 교육용 코드입니다. 실제 소자 안전 한계와 측정 장비 매뉴얼을 우선하세요.
