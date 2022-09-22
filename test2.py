from re import M
import warnings
import streamlit as st
import zipfile
import os
from streamlit.components.v1 import html
import time
warnings.filterwarnings("ignore")
import pandas


st.set_page_config(layout = 'wide')
st.markdown("<h1 style='text-align: center; '> One Click Deploy</h1>", unsafe_allow_html=True)
def app():
    """
    Main function call
    """
    new_script = f"<script>function removeFooter() {{ var ele = window.parent.document.getElementsByTagName('footer');if(ele.length>0){{ele[0].parentNode.removeChild(ele[0]);}}var ele1 = window.parent.document.getElementsByTagName('header');if(ele1.length>0){{ele1[0].parentNode.removeChild(ele1[0]);}}}}removeFooter();</script>"
    menu_script= f"""
      <script>
       function changeIcon() {{
            let parentNode = window.parent.document.querySelectorAll('[data-testid="stSidebar"]');
            let img = document.createElement('img');
            img.src="https://cadenz.ai/wp-content/uploads/2020/01/logo-black-.png";
            img.width=50;
            img.height=50;
            img.style="margin-left:10px; margin-top: 10px; margin-right: 10px;";
            img.className = "cadenz-logo";
            img.id= "cadenz";
            let img_lentra = document.createElement('img');
            img_lentra.src="https://www.lentra.ai/img/logo/logo.svg";
            	https://cdn.zeplin.io/605365812972634825c0e1ee/assets/eedbd48b-1758-4e33-9940-11420d63154d.svg
            img_lentra.width=100;
            img_lentra.height=50;
            img_lentra.style="margin-top: 10px; margin-right: 10px;";
            img_lentra.className = "lentra-logo";
            img_lentra.id= "lentra";
            let img_lentra_white = document.createElement('img');
            img_lentra_white.src="https://cdn.zeplin.io/605365812972634825c0e1ee/assets/eedbd48b-1758-4e33-9940-11420d63154d.svg";
            img_lentra_white.width=100;
            img_lentra_white.height=50;
            img_lentra_white.style="margin-top: 10px; margin-right: 10px;";
            img_lentra_white.className = "lentra-white-logo";
            img_lentra_white.id= "lentra-white";
            let sideBarNav = window.parent.document.querySelectorAll('[data-testid="stSidebarNav"]');
            if(sideBarNav.length > 0 && sideBarNav[0].querySelector("#lentra-white") == null){{
                sideBarNav[0].insertBefore(img_lentra_white, sideBarNav[0].firstChild);
            }}
            let iconDiv = document.createElement('div');
            iconDiv.style="display: flex; flex-direction: row;";
            iconDiv.append(img_lentra);
            iconDiv.append(img);
            console.log(parentNode)
            if(parentNode.length > 0) {{
                let bcContainer =parentNode[0].parentElement;
                if(bcContainer && bcContainer.querySelector("#cadenz") == null) {{
                    bcContainer.append(iconDiv)
                    bcContainer.setAttribute("style", "display:flex");
                }}
                let aNode = parentNode[0].children[1];
                svgel='<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="50" viewBox="0 0 50 50" style=" fill:#FD7E14;"><path d="M 0 7.5 L 0 12.5 L 50 12.5 L 50 7.5 Z M 0 22.5 L 0 27.5 L 50 27.5 L 50 22.5 Z M 0 37.5 L 0 42.5 L 50 42.5 L 50 37.5 Z"></path></svg>'
                let parser = new DOMParser();
                let doc = parser.parseFromString(svgel, "image/svg+xml");
                let iconButton = aNode.children[0];
                iconButton.replaceChildren(doc.firstChild);
                parentNode[0].children[1].removeChild(parentNode[0].children[1].firstChild);
                parentNode[0].children[1].append(iconButton);
            }}
            let recomIcon = document.createElement('span');
            recomIcon.className="css-8hkptd e1fb0mya0";
            recomIcon.id = "recomId"
            recomIcon.append("📈");
            let modelIcon = document.createElement('span');
            modelIcon.className="css-8hkptd e1fb0mya0";
            modelIcon.id = "modelId"
            modelIcon.append("📊");
            if(sideBarNav.length > 0) {{
                if(sideBarNav[0].children.length > 1 ) {{
                    let recomATagChild =  sideBarNav[0].children[1].firstChild.firstChild.firstChild;
                    if(recomATagChild.querySelector("#recomId") == null){{
                        recomATagChild.replaceChild(recomIcon, recomATagChild.firstChild);
                    }}
                    let modelATagChild = sideBarNav[0].children[1].children[2].firstChild.firstChild;
                    if(modelATagChild.querySelector("#modelId") == null){{
                        modelATagChild.replaceChild(modelIcon, modelATagChild.firstChild);
                    }}
                }}
            }}

        }}
        changeIcon();
        buttonNode= window.parent.document.querySelectorAll('[data-testid="stSidebar"]')
        function findParentByTagName(element, tagName) {{
        var parent = element;

            while (parent !== null && parent.tagName !== tagName.toUpperCase()) {{
                parent = parent.parentNode;
            }}

            return parent;
        }}

        function handleAnchorClick(event) {{
            event = event || window.event;

            if (findParentByTagName(event.target || event.srcElement, "A")) {{
                //event.preventDefault();
               buttonNode.length>0 ? buttonNode[0].firstChild.firstChild.firstChild.click() : "";
                console.log("An anchor was clicked!");
            }}
        }}

        window.parent.document.documentElement.addEventListener("click", handleAnchorClick, false);
    </script>
    """

    def add_script():
        html(menu_script, width=0, height=0)
        html(new_script, width=0, height=0)
    st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #FF6D00;
                color:#ffffff;
            }
            </style>""", unsafe_allow_html=True)

    st.markdown(
            """
        <style>
        .css-y3drt2:active, .css-y3drt2:visited, .css-y3drt2:hover {
            color: #d23439;
        }
        .css-10trblm {
            color: #173665;
        }
        thead > tr > th {
            background-color: rgb(255, 239, 222);
        }
        div[data-testid="stSidebarNav"] > ul > li > div > a {
            border-radius: 50px;
            width: 90%;
            margin-left: 20px;
            background-color: white;
            padding-left: 10px;
            margin-bottom: 20px;
            white-space: nowrap;
        } 
        section[data-testid="stSidebar"] > div {
            background-image: linear-gradient( to bottom right, #F0B27A , #EB984E, #85929E  60%);
        }
        .block-container.css-12oz5g7.egzxvld2 {
            padding: 0rem 1rem 0rem 1rem;
        }
        .stSelectbox > div > div {
            border-radius: 50px;
            border: 2px solid rgb(255, 109, 0);
            background-color: #fafafa;
            text-align: center;
        }
        .stfile_uploader > div > div {
            border-radius: 50px;
            border: 2px solid rgb(255, 109, 0);
            background-color: #fafafa;
            text-align: center;
        }
        thead, tbody, tfoot, tr, td, th {
            white-space: nowrap;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )       

    import os
    # stream = os.popen("tree/f")
    # output = stream.read()
    # st.write(output) 
    # print(output)

    # st.write(os.listdir())
    # import argparse


    def pro_bar():
        with st.spinner('Initializing...'):
            time.sleep(5)
        st.markdown(
        """
        <style>
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #FED8B1 , #FF8C00);
                text-align: center;
            }
        </style>""",
        unsafe_allow_html=True,
        )    
        latest_iteration = st.empty()
        bar = st.progress(0)
        time.sleep(1)
        bar.progress(20)
        latest_iteration.write("Logging in to AZURE...")
        time.sleep(5)
        bar.progress(40)
        latest_iteration.write("Creating Dockerfile...")
        time.sleep(5)
        bar.progress(60)
        latest_iteration.write("Building Image...")
        time.sleep(5)
        bar.progress(80)
        latest_iteration.write("Deploying...")
        time.sleep(5)
        bar.progress(100)
        latest_iteration.write("Almost Done...")
        time.sleep(5)
        
        # num = 20
        # for i in range(num):
        #     latest_iteration.write(f'{num - i} seconds left')
        #     bar.progress((100//num)*i)
        #     time.sleep(1)
        latest_iteration.empty() 
        bar.empty()  
        st.write("Done! Here is your link")
        st.write("https://fastapiapptdtdemo.azurewebsites.net/docs")

    def list_files(rootdir):
        #listdir() method returns a list of every file and folder in a directory. os. walk() function returns a list of every file in an entire file tree.
        #The walk () generates the output in three tuples, the path, directory, and the files that come in any subdirectory.
        new_title = '<p style="font-family:times new roman; color:Black; font-size: 20px;">Unzipped file contains</p>'
        st.sidebar.markdown(new_title, unsafe_allow_html=True)
        st.write(rootdir)
        for dirname, subdirs, files in os.walk(fr'{rootdir}'):
            level = dirname.replace(rootdir,"").count(os.sep)
            print(dirname)
            #print(list(os.walk(rootdir)))
            indent = " " * 4 * (level)
            #new_title = '<p style="font-family:times new roman; color:Black; font-size: 17px;">Folder_name :</p>'
            #st.sidebar.markdown(new_title, unsafe_allow_html=True)
            st.sidebar.write("📁{}{}".format(indent,os.path.basename(dirname)))
            #new_title = '<p style="font-family:times new roman; color:Black; font-size: 17px;">Files :</p>'
            #st.sidebar.markdown(new_title, unsafe_allow_html=True)
            subindent = "  " * 4 * (level + 1)
            for f in files: 
                st.sidebar.write(" ↳ 📄 {}{}".format(subindent,f))
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        #functions.unzip_files(uploaded_file)
        # with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        #     zip_ref.extractall()
        data = uploaded_file.getvalue()
        print(data)
        coeff_file = open('inference/coeff.json',"r")
        filename= os.path.splitext(filename)[0]
        print(filename)
        #print(uploaded_file)
        # folders can be display only files not possible
        path = r"C:\Users\Dell Laptop\Python\env\Docker\Oneclick\one-click-v4"
        rootdir = os.path.join(path,filename)
        list_files(rootdir)
        #tab = os.listdir(rootdir).columns = ["Files and Folders"]
        #st.sidebar.write(os.listdir(rootdir))
        #print(rootdir)
        # for dirName, subdirList, fileList in os.walk(rootdir):
        #     for fname in fileList:
        #         print('\t%s' % fname)        
        #path = 'VF_Recommendation_POC-5\cluster results'
        #dir_list = os.listdir(path)
        st.warning("Files Unzipped!")
        #st.write(list(dir_list))
        if st.button("Deploy"):   
            #functions.redeploy()
            st.write("Done! Here is your link")
            st.write("https://fastapiapptdtdemo.azurewebsites.net/docs")
                #pro_bar()
      
    add_script()

if __name__ == "__main__":
    app()

