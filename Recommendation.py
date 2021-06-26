#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


df = pd.read_excel("data.xlsx")
df


# In[21]:


df['표준산업분류명'].value_counts()


# In[22]:


from geopy import distance

def dist_calc (df):
    start = (37.50742913954131, 126.95846245162767)
    stop = (df['위도'], df['경도'])
    return distance.great_circle(start, stop).km * 1000
df['distance1'] = df.apply (lambda df: dist_calc (df), axis=1)

def dist_calc (df):
    start = (37.50730896008081, 126.95734305559398)
    stop = (df['위도'], df['경도'])
    return distance.great_circle(start, stop).km * 1000
df['distance2'] = df.apply (lambda df: dist_calc (df), axis=1)

def dist_calc (df):
    start = (37.505454071005246, 126.95367913231576)
    stop = (df['위도'], df['경도'])
    return distance.great_circle(start, stop).km * 1000
df['distance3'] = df.apply (lambda df: dist_calc (df), axis=1)


# In[23]:


df_food = df[(df['표준산업분류명'] == '한식 음식점업') | (df['표준산업분류명'] == '분식 및 김밥 전문점') | (df['표준산업분류명'] == '서양식 음식점업')
             | (df['표준산업분류명'] == '중식 음식점업')| (df['표준산업분류명'] == '일식 음식점업')| (df['표준산업분류명'] == '피자, 햄버거, 샌드위치 및 유사 음식점업')
             | (df['표준산업분류명'] == '그외 기타 음식점업')| (df['표준산업분류명'] == '기관구내식당업')| (df['표준산업분류명'] == '기타 외국식 음식점업')
             | (df['표준산업분류명'] == '치킨 전문점')]


# In[24]:


df_cafe = df[(df['표준산업분류명'] == '비알콜 음료점업') | (df['표준산업분류명'] == '제과점업')]


# In[25]:


df_alcohol = df[(df['표준산업분류명'] == '기타 주점업') | (df['표준산업분류명'] == '일반유흥 주점업')]


# In[26]:


#longtitude = df['경도']
#latitude = df['위도']


# In[27]:


food1 = df_food[df_food.distance1 < 500]
food2 = df_food[df_food.distance2 < 500]
food3 = df_food[df_food.distance3 < 500]

cafe1 = df_cafe[df_cafe.distance1 < 500]
cafe2 = df_cafe[df_cafe.distance2 < 500]
cafe3 = df_cafe[df_cafe.distance3 < 500]

alcohol1 = df_alcohol[df_alcohol.distance1 < 500]
alcohol2 = df_alcohol[df_alcohol.distance2 < 500]
alcohol3 = df_alcohol[df_alcohol.distance3 < 500]


# In[28]:


import folium
from folium.plugins import MarkerCluster


def mapping(x):
  map = folium.Map(location = [37.50566653486357, 126.9571440782172], zoom_start = 17)
  list1=[]
  list2=[]
  marker_cluster = MarkerCluster().add_to(map)

  for a in x.index:
      folium.Marker(location = [x.loc[a,"위도"],x.loc[a,"경도"]],
                  popup=x.loc[a,"상호명"]).add_to(marker_cluster)
      list1.append(x.loc[a,"위도"])
      list2.append(x.loc[a,"경도"])
  return map


# In[29]:


mapping(food1)


# In[30]:


mapping(food2)


# In[31]:


mapping(food3)


# In[32]:


mapping(cafe1)


# In[33]:


mapping(cafe2)


# In[34]:


mapping(cafe3)


# In[35]:


mapping(alcohol1)


# In[36]:


mapping(alcohol2)


# In[37]:


mapping(alcohol3)


# In[38]:


async def 정문주변음식점(ctx):
    await ctx.send(f'정문주변음식점을 찾은 결과입니다 {mapping(food1)}')

async def 정문주변카페(ctx):
    await ctx.send(f'정문주변카페를 찾은 결과입니다 {mapping(cafe1)}')
    
async def 정문주변주점(ctx):
    await ctx.send(f'정문주변주점을 찾은 결과입니다 {mapping(alcohol1)}')
    

async def 중문주변음식점(ctx):
    await ctx.send(f'정문주변음식점을 찾은 결과입니다 {mapping(food2)}')
    
async def 중문주변카페(ctx):
    await ctx.send(f'정문주변카페를 찾은 결과입니다 {mapping(cafe2)}')
    
async def 중문주변주점(ctx):
    await ctx.send(f'정문주변주점을 찾은 결과입니다 {mapping(alcohol2)}')
    
    
async def 후문주변음식점(ctx):
    await ctx.send(f'정문주변음식점을 찾은 결과입니다 {mapping(food3)}')
    
async def 후문주변카페(ctx):
    await ctx.send(f'정문주변카페를 찾은 결과입니다 {mapping(cafe3)}')
    
async def 후문주변주점(ctx):
    await ctx.send(f'정문주변주점을 찾은 결과입니다 {mapping(alcohol3)}')


# In[ ]:




