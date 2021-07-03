#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_excel("data.xlsx")
df


# In[7]:


df['표준산업분류명'].value_counts()


# In[8]:


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


# In[9]:


df_food = df[(df['표준산업분류명'] == '한식 음식점업') | (df['표준산업분류명'] == '분식 및 김밥 전문점') | (df['표준산업분류명'] == '서양식 음식점업')
             | (df['표준산업분류명'] == '중식 음식점업')| (df['표준산업분류명'] == '일식 음식점업')| (df['표준산업분류명'] == '피자, 햄버거, 샌드위치 및 유사 음식점업')
             | (df['표준산업분류명'] == '그외 기타 음식점업')| (df['표준산업분류명'] == '기관구내식당업')| (df['표준산업분류명'] == '기타 외국식 음식점업')
             | (df['표준산업분류명'] == '치킨 전문점')]


# In[10]:


df_cafe = df[(df['표준산업분류명'] == '비알콜 음료점업') | (df['표준산업분류명'] == '제과점업')]


# In[11]:


df_alcohol = df[(df['표준산업분류명'] == '기타 주점업') | (df['표준산업분류명'] == '일반유흥 주점업')]


# In[12]:


#longtitude = df['경도']
#latitude = df['위도']


# In[13]:


food1 = df_food[df_food.distance1 < 500]
food2 = df_food[df_food.distance2 < 500]
food3 = df_food[df_food.distance3 < 500]

cafe1 = df_cafe[df_cafe.distance1 < 500]
cafe2 = df_cafe[df_cafe.distance2 < 500]
cafe3 = df_cafe[df_cafe.distance3 < 500]

alcohol1 = df_alcohol[df_alcohol.distance1 < 500]
alcohol2 = df_alcohol[df_alcohol.distance2 < 500]
alcohol3 = df_alcohol[df_alcohol.distance3 < 500]


# In[14]:


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


# In[68]:


mapping(food1)


# In[69]:


mapping(food2)


# In[70]:


mapping(food3)


# In[71]:


mapping(cafe1)


# In[72]:


mapping(cafe2)


# In[73]:


mapping(cafe3)


# In[74]:


mapping(alcohol1)


# In[75]:


mapping(alcohol2)


# In[76]:


mapping(alcohol3)


# In[101]:


from PIL import Image
 
image = Image.open("figure_food1.png")
showimage1 = image.show()
showimage1


# In[98]:


image = Image.open("figure_food2.png")
showimage2 = image.show()
showimage2


# In[85]:


image = Image.open("figure_food3.png")
showimage3 = image.show()
showimage3


# In[86]:


image = Image.open("figure_cafe1.png")
showimage4 = image.show()
showimage4


# In[87]:


image = Image.open("figure_cafe2.png")
showimage5 = image.show()
showimage5


# In[97]:


image = Image.open("figure_cafe3.png")
showimage6 = image.show()
showimage6


# In[89]:


image = Image.open("figure_alcohol1.png")
showimage7 = image.show()
showimage7


# In[90]:


image = Image.open("figure_alcohol2.png")
showimage8 = image.show()
showimage8


# In[96]:


image = Image.open("figure_alcohol3.png")
showimage9 = image.show()
showimage9


# In[52]:


food1 = food1.sort_values('distance1')
food1


# In[18]:


food2 = food2.sort_values('distance2')
food2


# In[53]:


food3 = food3.sort_values('distance3')
food3


# In[55]:


cafe1 = cafe1.sort_values('distance1')
cafe1


# In[56]:


cafe2 = cafe2.sort_values('distance2')
cafe2


# In[57]:


cafe3 = cafe3.sort_values('distance3')
cafe3


# In[58]:


alcohol1 = alcohol1.sort_values('distance1')
alcohol1


# In[59]:


alcohol2 = alcohol2.sort_values('distance2')
alcohol2 


# In[60]:


alcohol3 = alcohol3.sort_values('distance3')
alcohol3


# In[102]:

def getResult(where, what):
    dataReturn = []

    if where == "정문":
        if what == "음식점":
            dataReturn.append("figure_food1.png")
            dataReturn.append(food1.values.tolist())
        elif what == "카페":
            dataReturn.append("figure_cafe1.png")
            dataReturn.append(cafe1.values.tolist())
        elif what == "주점":
            dataReturn.append("figure_alcohol1.png")
            dataReturn.append(alcohol1.values.tolist())
    elif where == "중문":
        if what == "음식점":
            dataReturn.append("figure_food2.png")
            dataReturn.append(food2.values.tolist())
        elif what == "카페":
            dataReturn.append("figure_cafe2.png")
            dataReturn.append(cafe2.values.tolist())
        elif what == "주점":
            dataReturn.append("figure_alcohol2.png")
            dataReturn.append(alcohol2.values.tolist())
    elif where == "후문":
        if what == "음식점":
            dataReturn.append("figure_food3.png")
            dataReturn.append(food3.values.tolist())
        elif what == "카페":
            dataReturn.append("figure_cafe3.png")
            dataReturn.append(cafe3.values.tolist())
        elif what == "주점":
            dataReturn.append("figure_alcohol3.png")
            dataReturn.append(alcohol3.values.tolist())

    return dataReturn

async def 정문주변음식점(ctx):
    await ctx.send(f'정문주변음식점을 찾은 결과입니다 {food1},{showimage1}')

async def 정문주변카페(ctx):
    await ctx.send(f'정문주변카페를 찾은 결과입니다 {cafe1},{showimage4}')
    
async def 정문주변주점(ctx):
    await ctx.send(f'정문주변주점을 찾은 결과입니다 {alcohol1},{showimage7}')
    

async def 중문주변음식점(ctx):
    await ctx.send(f'중문주변음식점을 찾은 결과입니다 {food2},{showimage2}')
    
async def 중문주변카페(ctx):
    await ctx.send(f'중문주변카페를 찾은 결과입니다 {cafe2},{showimage5}')
    
async def 중문주변주점(ctx):
    await ctx.send(f'중문주변주점을 찾은 결과입니다 {alcohol2},{showimage8}')
    
    
async def 후문주변음식점(ctx):
    await ctx.send(f'후문주변음식점을 찾은 결과입니다 {food3},{showimage3}')
    
async def 후문주변카페(ctx):
    await ctx.send(f'후문주변카페를 찾은 결과입니다 {cafe3},{showimage6}')
    
async def 후문주변주점(ctx):
    await ctx.send(f'후문주변주점을 찾은 결과입니다 {alcohol3},{showimage9}')


# In[ ]:




