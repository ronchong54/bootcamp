import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
#venv\Scripts\activate


st.title("Test - App")
X = np.random.normal(0,10, size =(100,2))

fig, ax = plt.subplots(1,2,figsize=(10,6))

ax[0].hist(X[::,0], color = 'red', alpha = 0.4)
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].set_title("X1", size = 14)
ax[1].hist(X[::,1], color = 'orange', alpha = 0.6)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].set_title("X2", size = 14)
st.pyplot(fig)