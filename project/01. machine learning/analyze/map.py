import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
merged_df = pd.read_csv('project/01. machine learning/data/education/merged_data.csv')

# 수치형 열 변환 및 NaN 처리
numeric_columns = ['유치원', '초등학교', '중학교', '고등학교']
for col in numeric_columns:
    non_numeric = merged_df[col].apply(lambda x: isinstance(x, str))
    if non_numeric.any():
        print(f"Non-numeric values in {col}:")
        print(merged_df[non_numeric][col])
        
    merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')

# NaN 값 제거
merged_df.dropna(subset=numeric_columns, inplace=True)

# 총학생수 계산
merged_df['총학생수'] = merged_df[numeric_columns].sum(axis=1)

# 지역별 총학생수 집계
region_data = merged_df.groupby('지역별')['총학생수'].sum().reset_index()

# 대한민국 지도 데이터 로드
shapefile_path = "map/ne_110m_admin_0_countries.shp"
korea_map = gpd.read_file(shapefile_path)
korea_map = korea_map[korea_map['ADMIN'] == 'South Korea']

# 지역 이름 매핑
region_mapping = {
    '서울': 'Seoul',
    '부산광역시': 'Busan',
    '대구광역시': 'Daegu',
    '인천광역시': 'Incheon',
    '광주광역시': 'Gwangju',
    '대전광역시': 'Daejeon',
    '울산광역시': 'Ulsan',
    '세종특별자치시': 'Sejong',
    '경기도': 'Gyeonggi',
    '강원특별자치도': 'Gangwon',
    '충청북도': 'Chungbuk',
    '충청남도': 'Chungnam',
    '전북특별자치도': 'Jeonbuk',
    '전라남도': 'Jeonnam',
    '경상북도': 'Gyeongbuk',
    '경상남도': 'Gyeongnam',
    '제주특별자치도': 'Jeju'
}

# region_data에 매핑된 지역 열 추가
region_data['mapped_region'] = region_data['지역별'].map(region_mapping)

# korea_map과 region_data 병합
korea_map = korea_map.merge(region_data[['mapped_region', '총학생수']],
                             left_on='ADMIN', right_on='mapped_region', how='left')

# NaN 값을 0으로 대체
korea_map['총학생수'] = korea_map['총학생수'].fillna(0)

# 지도 시각화
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
korea_map.boundary.plot(ax=ax, linewidth=1)

# 총학생수에 따라 색상으로 채우기
korea_map.plot(column='총학생수', ax=ax, legend=True,
               cmap='OrRd', edgecolor='black',
               missing_kwds={'color': 'lightgrey', 'label': 'No data'})

# 제목 및 레이블 추가
plt.title('지역별 총학생수', fontsize=15)
plt.xlabel('경도', fontsize=12)
plt.ylabel('위도', fontsize=12)

# 시각화 출력
plt.show()