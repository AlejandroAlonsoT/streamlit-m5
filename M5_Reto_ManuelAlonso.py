import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt


st.title('Employees app')
st.header('M5 Reto de Aplicacion Manuel Alonso')
st.text('Se utliza este espacio para desarrollar el reto de aplicacion del M5')

@st.cache
def load_data(nrows = 500):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

@st.cache
def filter_data_by_id(id):
    filtered_data_id = data[data['Employee_ID'].str.upper().str.contains(id)]
    return filtered_data_id

@st.cache
def filter_data_by_hometown(hometown):
    filtered_data_hometown = data[data['Hometown'].str.upper().str.contains(hometown)]
    return filtered_data_hometown

@st.cache
def filter_data_by_unit(unit):
    filtered_data_unit = data[data['Unit'].str.upper().str.contains(unit)]
    return filtered_data_unit

@st.cache
def filter_data_by_educationLevel(edLevel):
    filtered_data_edLevel = data[data['Education_Level'] == edLevel]
    return filtered_data_edLevel

@st.cache
def filter_data_by_selected_hometown(hometown):
    filtered_data_hometown = data[data['Hometown'] == hometown]
    return filtered_data_hometown

@st.cache
def filter_data_by_selected_unit(unit):
    filtered_data_unit = data[data['Unit'] == unit]
    return filtered_data_unit



data = load_data(1000)
st.sidebar.header('Sidebar')
if st.sidebar.checkbox('Mostrar registros de empleados completo'):
    st.subheader('Registros Empleados')
    st.write(data)


employeeId = st.sidebar.text_input('ID Employee')
btnId = st.sidebar.button('Buscar ID')

if btnId:
    data_id = filter_data_by_id(employeeId.upper())
    count_row = data_id.shape[0]  # Gives number of rows
    st.write(f"Total empleados mostrados : {count_row}")
    st.write(data_id)

hometownInput = st.sidebar.text_input('Employe hometown')
btnHometown = st.sidebar.button('Buscar Hometown')

if btnHometown:
    data_hometown = filter_data_by_hometown(hometownInput.upper())
    count_row = data_hometown.shape[0]  # Gives number of rows
    st.write(f"Total de origenes de empleados : {count_row}")
    st.write(data_hometown)

employeeUnit = st.sidebar.text_input('Employee Unit')
btnUnit = st.sidebar.button('Buscar Unit')

if btnUnit:
    data_Unit = filter_data_by_unit(employeeUnit.upper())
    count_row = data_Unit.shape[0]  # Gives number of rows
    st.write(f"Total de origenes de empleados : {count_row}")
    st.write(data_Unit)


selected_edLevel = st.sidebar.selectbox("Seleccionar Nivel educacion", data['Education_Level'].unique())
btnFilterbyEdLevel = st.sidebar.button('Filtrar Nivel Educacion ')

if btnFilterbyEdLevel:
    filterbyEdLevel = filter_data_by_educationLevel(selected_edLevel)
    count_row = filterbyEdLevel.shape[0]  # Gives number of rows
    st.write(f"Empleados con el nivel de educacion : {count_row}")
    st.write(filterbyEdLevel)

selected_hometown = st.sidebar.selectbox("Seleccionar Hometown", data['Hometown'].unique())
btnFilterbyHometown = st.sidebar.button('Filtrar Hometown')

if btnFilterbyHometown:
    filterbyHometown = filter_data_by_selected_hometown(selected_hometown)
    count_row = filterbyHometown.shape[0]  # Gives number of rows
    st.write(f"Empleados de la ciudad seleccionada : {count_row}")
    st.write(filterbyHometown)

selected_unit = st.sidebar.selectbox("Seleccionar Unit", data['Unit'].unique())
btnFilterbyUnit = st.sidebar.button('Filtrar Unit')

if btnFilterbyUnit:
    filterbyUnit = filter_data_by_selected_unit(selected_unit)
    count_row = filterbyUnit.shape[0]  # Gives number of rows
    st.write(f"Empleados de la unidad seleccionada : {count_row}")
    st.write(filterbyUnit)

    #Grafica del punto 14 del reto si quisieramos mostrar en sync con este filtro
    #fig2, ax2 = plt.subplots()
    #ax2.hist(filterbyUnit['Hometown'])
    #st.header("Grafica Frecuencia de Unidad: Empleado por ciudad")
    #st.text(selected_unit)
    #st.pyplot(fig2)


fig, ax = plt.subplots()
ax.hist(data['Age'])
st.header("Histograma de Edades Empleado")
st.pyplot(fig)

fig2, axs2 = plt.subplots(3,4,figsize=(15,12))
plt.subplots_adjust(wspace=0.5)
columns = data['Unit'].unique()
for column, ax in zip(columns, axs2.ravel()):
    dataUnit = filter_data_by_selected_unit(column)
    ax.hist(dataUnit['Hometown'])
    ax.tick_params(rotation=50)
    ax.set_title(column)

st.header("Grafica Frecuencia de Unidad: Empleado por ciudad")
st.pyplot(fig2)



fig3, axs3 = plt.subplots()
attrition_by_hometown = data[['Hometown','Attrition_rate']]
axs3.bar(attrition_by_hometown['Hometown'], attrition_by_hometown['Attrition_rate'])
axs3.tick_params(rotation=90)
st.header("Grafica Indices de decersion por Hometown")
st.pyplot(fig3)

fig4, axs4 = plt.subplots()
attrition_by_age = data[['Age','Attrition_rate']].groupby('Age').mean()
axs4.bar(attrition_by_age.index, attrition_by_age['Attrition_rate'])
axs4.tick_params(rotation=90)
st.header("Grafica Indices de decercion promedio por Edad")
st.pyplot(fig4)

fig5, axs5 = plt.subplots()
attrition_by_timeService = data[['Time_of_service','Attrition_rate']]
axs5.scatter(x=attrition_by_timeService['Time_of_service'], y=attrition_by_timeService['Attrition_rate'])
axs5.tick_params(rotation=90)
st.header("Grafica relacion entre tiempo de servicio y decercion")
st.pyplot(fig5)