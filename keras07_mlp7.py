# x의 열은 1개
# y의 열은 3개

import numpy as np  
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. 데이터
x = np.array([range(10)])    # (1, 10)
x = x.T   # (10, 1)

y = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
              [9,8,7,6,5,4,3,2,1,0]]) # (3, 10)

y = y.T     #(10, 3)

# [실습]
# 예측 : [[9, 30, 210]] 

#2.  모델구성
model = Sequential()
model.add(Dense(10, input_dim=1))
model.add(Dense(100))
model.add(Dense(1000))
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(3))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=1000, batch_size=1)

#4. 평가, 예측
loss = model.evaluate(x, y)
print("loss : ", loss)

result = model.predict([[9]])
print("[[9]]의 예측값 : ", result)


"""
loss :  1.313675080175103e-12
1/1 [==============================] - 0s 84ms/step
[[9]]의 예측값 :  [[1.0000001e+01 1.9000002e+00 2.0712614e-06]]

([10,100,1000,100,10,3], mse, adam, 1000, 1)
"""