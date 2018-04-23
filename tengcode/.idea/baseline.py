# coding=utf-8
# @author:bryan
# blog: https://blog.csdn.net/bryan__
# github: https://github.com/YouChouNoBB/2018-tencent-ad-competition-baseline
import pandas as pd
import lightgbm as lgb
#from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from scipy import sparse
import os

ad_feature=pd.read_csv('../data2/adFeature.csv')
user_feature=pd.read_csv('../data2/userFeature.csv')
train=pd.read_csv('../data2/train.csv')
#print(train)
predict=pd.read_csv('../data2/test1.csv')
#print(predict)
train.loc[train['label']==-1,'label']=0 #把label是1的变成0
#print(train)
predict['label']=-1#把预测label是都变成-1
#print(predict)
data=pd.concat([train,predict])#把两个文件合在一列中变成一个dataframe
#print(data)
data=pd.merge(data,ad_feature,on='aid',how='left')#把data和ad__feature和在一起左外连接得到 当两者aid相等的时候
#print(data.head())
data=pd.merge(data,user_feature,on='uid',how='left')#把data和user__feature和在一起左外连接得到 当两者uid相等的时候
#print(data.head())
data=data.fillna('-1')#把为nan的缺失值都填充为-1
#print(data.head())
#print(data.columns)
one_hot_feature=['LBS','age','carrier','consumptionAbility','education','gender','house','os','ct',
                 'marriageStatus','advertiserId','campaignId', 'creativeId',
       'adCategoryId', 'productId', 'productType']#独热编码的类别特征是这些 少了一个creativeSize特征没用
vector_feature=['appIdAction','appIdInstall','interest1','interest2','interest3','interest4',
                'interest5','kw1','kw2','kw3','topic1','topic2','topic3']#集合特征
for feature in one_hot_feature:
    try:
        data[feature] = LabelEncoder().fit_transform(data[feature].apply(int))#简单来说 LabelEncoder 是对不连续的数字或者文本进行编号
    except:
        data[feature] = LabelEncoder().fit_transform(data[feature])#主要的作用是对类别特征编码
print(data.head())
#print(data)
train=data[data.label!=-1]#刚才label设置-1的目的是为了标记他是test 只要把不是-1找出来就是train了
#print(train)
train_y=train.pop('label')#train把label取出来就是对应的标签
#print(train_y)
# train, test, train_y, test_y = train_test_split(train,train_y,test_size=0.2, random_state=2018)
test=data[data.label==-1]#刚才label设置-1的目的是为了标记他是test 只要是-1找出来就是test了
res=test[['aid','uid']]#把test的aid和uid单独拿出来
test=test.drop('label',axis=1)#test把label那一列删除
#print(test)
enc = OneHotEncoder()#onehot
train_x=train[['creativeSize']]#刚才没处理的连续型数据<class 'pandas.core.frame.DataFrame'>
#train_x2=train['creativeSize']#类型不一样<class 'pandas.core.series.Series'>
#print(type(train_x2))
test_x=test[['creativeSize']]
#print(test_x)

for feature in one_hot_feature:
    enc.fit(data[feature].values.reshape(-1, 1))
    # print(feature)#LBS
    # print(data[feature].values)#[0 0 0 ... 0 0 0]
    # print(data[feature].values.reshape(-1, 1))#把1行N列变成了N行一列
    #print(enc.fit(data[feature].values.reshape(-1, 1)))
    train_a=enc.transform(train[feature].values.reshape(-1, 1))
    # print(train_a)
    # print(type(train_a))
    train_x= sparse.hstack((train_x, train_a)) #scipy.sparse 稀疏矩阵 sparse.hstack横向合并train_x和train_a
    # print(train_x)
    test_a = enc.transform(test[feature].values.reshape(-1, 1))
    test_x = sparse.hstack((test_x, test_a))
print('one-hot prepared !')#完成独热编码
cv=CountVectorizer()
for feature in vector_feature:
    cv.fit(data[feature])
    # print(feature)
    train_a = cv.transform(train[feature])
    train_x = sparse.hstack((train_x, train_a))#scipy.sparse 稀疏矩阵 sparse.hstack横向合并train_x和train_a
    print(train_a) #CountVectorizer()通过这个把特征变成 次数文本向量
    test_a = cv.transform(test[feature])
    test_x = sparse.hstack((test_x, test_a))
print('cv prepared !') #文本表示成了向量

def LGB_test(train_x,train_y,test_x,test_y):
    print("LGB test")
    clf = lgb.LGBMClassifier(
        boosting_type='gbdt', num_leaves=31, reg_alpha=0.0, reg_lambda=1,
        max_depth=-1, n_estimators=1000, objective='binary',
        subsample=0.7, colsample_bytree=0.7, subsample_freq=1,
        learning_rate=0.05, min_child_weight=50,random_state=2018,n_jobs=-1
    )
    #初始化lgb的参数
    clf.fit(train_x, train_y,eval_set=[(train_x, train_y),(test_x,test_y)],eval_metric='auc',early_stopping_rounds=100)
    #fit一下
    print(clf.feature_importances_)#输出特征重要度
    return clf,clf.best_score_[ 'valid_1']['auc'] #输出auc得分

def LGB_predict(train_x,train_y,test_x,res):#实现预测
    print("LGB test")
    clf = lgb.LGBMClassifier(
        boosting_type='gbdt', num_leaves=31, reg_alpha=0.0, reg_lambda=1,
        max_depth=-1, n_estimators=1500, objective='binary',
        subsample=0.7, colsample_bytree=0.7, subsample_freq=1,
        learning_rate=0.05, min_child_weight=50, random_state=2018, n_jobs=-1
    )
    clf.fit(train_x, train_y, eval_set=[(train_x, train_y)], eval_metric='auc',early_stopping_rounds=100)
    #fit一下 eval_set 评价得分的集合 标准auc early_stopping
    res['score'] = clf.predict_proba(test_x)[:,1]
    res['score'] = res['score'].apply(lambda x: float('%.6f' % x))
    res.to_csv('../data2/submission.csv', index=False)
    os.system('zip ../data2/baseline.zip ../data2/submission.csv')
    return clf

model=LGB_predict(train_x,train_y,test_x,res)
#预测