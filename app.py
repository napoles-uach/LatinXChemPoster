import streamlit as st
from stmol import showmol,render_pdb,render_pdb_resn
import py3Dmol
st.set_page_config(layout="wide")
col1,cola,col2,colb,col3 = st.columns([1,1,6,1,1])
col1.image("Plano.png", width=100)
col3.image("ltnx.jpeg", width=100)
with col2:
    st.write("# Stmol component: Easy molecular visualization in Streamlit web apps :boat:")
    st.sidebar.write("José Manuel Nápoles-Duarte*, Juan Pedro Palomares-Baez, Marco Antonio Chavez Rojo, Luz María Rodriguez-Valdez, Avratanu Biswas, Mitchell Parker")
    st.sidebar.text("Facultad de Ciencias Quimicas, Universidad Autonoma de Chihuahua")

    with st.expander("Abstract",expanded=True):
        
        st.error("""
        :+1: In this work we present Stmol, a custom component for introducing molecular 3D visualizations in Streamlit web apps. Stmol depends on the popular package Py3DMol and is intended for helping computational chemists and biologists to disseminate recent results or as complements to academic articles in an easy way. With Stmol the user can visualize standard file formats like xyz, mol, pdb, cube, among others. Currently it is the preferred way to deploy molecular models by scientists using Streamlit.
    """)

frame1, frame2,frame3 = st.columns([1,1,1])
with frame1:
    with st.expander("Introduction",expanded=True):
        st.info("""
        Visualization of molecular models is a very important task
        that allows to analyse molecular structures. Normaly this is something that
        is done in a local computer, but when it is desired to communicate new findings, the use of web applications
        is of great help.

        Here we present to the **LatinXChem** community the **Stmol** component. 

        """)

with frame2:
    with st.expander("Running Stmol",expanded=True):
        st.success("""
    In order to deploy 3d molecular structures in Streamlit,
    it is necesary to install Streamlit and Stmol.
    After that an app.py file can be run.
    """)
        code = '''pip install streamlit
pip install stmol
streamlit run app.py'''
        st.code(code, language='bash')
        st.image("https://www.frontiersin.org/files/Articles/990846/fmolb-09-990846-HTML/image_m/fmolb-09-990846-g002.jpg")


with frame3:
    with st.expander("Example",expanded=True):
        #st.error("""
        #For more details on the code, check the paper: 
        #[ ![](https://img.shields.io/badge/Paper-Frontiers-red) ](https://www.frontiersin.org/articles/10.3389/fmolb.2022.990846/full)
        #""")
        code2="""
import streamlit as st
import py3Dmol
from stmol import showmol
st.sidebar.title('Show Proteins')
prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
prot_list=prot_str.split(',')
bcolor = st.sidebar.color_picker('Pick A Color', '#00f900')
protein=st.sidebar.selectbox('select protein',prot_list)
style = st.sidebar.selectbox('style',['line','cross','stick','sphere','cartoon'])
xyzview = py3Dmol.view(query='pdb:'+protein)
xyzview.setStyle({style:{'color':'spectrum'}})
xyzview.setBackgroundColor(bcolor)
xyzview.zoomTo()
showmol(xyzview,height=500,width=800)"""
        st.code(code2,language="python")

bar1,bar2 = st.columns([3,5])
bar1.title('Show Proteins')
prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
prot_list=prot_str.split(',')
bcolor = bar1.color_picker('Pick A Color', '#FADBD8')
protein=bar1.selectbox('select protein',prot_list)
style = bar1.selectbox('style',['cartoon','cross','stick','sphere','line'])
spin = bar1.checkbox('Spin', value = True)
xyzview = py3Dmol.view(query='pdb:'+protein)
xyzview.setStyle({style:{'color':'spectrum'}})
xyzview.setBackgroundColor(bcolor)
if spin:
    xyzview.spin(True)
else:
    xyzview.spin(False)
xyzview.zoomTo()
with bar2:
    showmol(xyzview,height=500,width=550)

with st.expander("Conclusions",expanded=True):
    st.success('''As Stmol is based on Py3Dmol libray, it offers great flexibility to deploy 
    complex structures, and at the same time is easy to implement *python*
    scripts as web apps. 
    Further improvements are on the way of the Stmol library. 
    ''')
    st.error('''
    References:

    1) Stmol: A component for building interactive molecular visualizations within streamlit web-applications. Front. Mol. Biosci., 23 September 2022 https://doi.org/10.3389/fmolb.2022.990846
    2) Github repo: https://github.com/napoles-uach/stmol
    3) Blog post: https://medium.com/p/657d28152753
    ''')
end=st.button("The end")
if end:
    st.balloons()
