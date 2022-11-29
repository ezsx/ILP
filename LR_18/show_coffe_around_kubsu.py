import folium
import osmnx as ox

# Отображаем все кофейни в радиусе 500m от КубГУ

# Записываем координаты кубгу (это можно сделать и другими способами)
# ул. Ставропольская, 149, Краснодар, Краснодарский край, 350040, Россия
coordinates = [45.020844611097225, 39.031289040117294]
# инициализируем карту
m = folium.Map(location=coordinates, zoom_start=15, tiles='cartodbpositron')
# (необязательно) рисуем плот нашей местности
buildings = ox.geometries_from_point(coordinates, tags={'building': True})
plt = buildings.plot()
plt.figure.savefig('area.png')
# (необязательно) включаем логи
ox.config(log_console=True, use_cache=True)
#  выбираем данные которые нам нужны
# (amenity - тип объекта, name - название объекта, cuisine - тип кухни (в нашем случае это кофейня))
tags = {'amenity': 'cafe', 'cuisine': 'coffee_shop'}
# выбираем радиус в котором будем искать объекты (500 метров)
gdf = ox.geometries_from_point(coordinates, tags=tags, dist=500, )
# сохраняем найденные объекты в переменную
points = gdf['geometry'].tolist()
# рисуем найденные объекты на карте проходя по списку points (список координат кофейен)
for point in points:
    coffe_name_current = gdf[gdf['geometry'] == point]['name'].values[0]
    # к сожалению folium поддерживает только  FontAwesome 4 , поэтому мы ограаничены выбором иконок sadCat
    folium.Marker(location=[point.y, point.x], icon=folium.Icon(color='cadetblue', icon="coffee", prefix='fa'),
                  popup=coffe_name_current).add_to(m)
# сохраняем карту в html файл
m.save('coffe.html')
print('Done')
