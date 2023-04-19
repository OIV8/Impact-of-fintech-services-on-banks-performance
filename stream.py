#######################################
############## STREAMLIT ##############
#######################################
from thesis import *
import streamlit as st

####### LAYOUT #######
st.set_page_config(layout="wide")
st.write(
        """
        <style>
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .reportview-container .main .block-container{{
                max-width: {max_width}px;
                padding-top: {padding_top}rem;
                padding-right: {padding_right}rem;
                padding-left: {padding_left}rem;
                padding-bottom: {padding_bottom}rem;
        }}
        </style> 
        """, unsafe_allow_html=True)

####### TITLE #######
st.title('Impact of FinTech services on banks performance')
st.write(
        '''The aim of this study is to investigate the relationship
        between the development of fintech services by banks
        and the profitability of banks, through a regression
        analysis that is built on an unbalanced panel data set.
        In addition, the pandemic factor is being studied to
        highlight its effect on the results.  
        The sample of this panel consisted of 12 italian banks, each
        of them annually observed over a period of 8 years, 
        from 2014 to 2021. The critierion to select the banks is
        that every bank must be quoted on the Italian Stock Exchange
        for at least seven years.  
        The main source is BankFocuse, while the contry-level data 
        were obtaied from World Bank. 
        ''')

####### VARIABLE DESCRIPTION #######
st.write(
        '''
        ---
        ## Variable Description
        ''')
var = ( 'ROA', 'ROE', 'FS', 'DUMMY', 'BS', 'ID', 'LSIZE', 'CAP', 'LOAN', 'LLP', 'NONIN',
        'GDP', 'INF', 'Z_SCORE', '' )
sel_var = st.selectbox('Pick the variable to see its description', var, index = 14)
def selectvar():
        if sel_var == 'ROA':
                st.write(r'''
                        - **The variable :green[ROA] (Return On Assets) is a financial ratio that measures the profitability of the bank 
                        in relation to its total assets. It's a variable calculated by dividing the bank's net income by its total assets:**  
                        $$
                        \text{ROA} = \frac{\text{Net Income}}{\text{Total Assets}}
                        $$''')
        elif sel_var == 'ROE':
                st.write(r'''
                        - **The variable :green[ROE] (Return On Equity) is a financial ratio that measures the profitability of shareholder's
                        equity. It's a variable calculated by dividing the bank's net income by its equity:**  
                        $$
                        \text{ROE} = \frac{\text{Net Income}}{\text{Equity}}
                        $$''')
        elif sel_var == 'FS':
                st.write(r'''
                        - **The variable :green[FS] (Fintech Score) measures the development of fintech services by the bank. In more detail,
                        were created seven dummy variables, one for each category of service. Each variable got a value of 1 if the bank 
                        provided that service in that year, and 0 otherwise. Later these seven variables were summed up to determine the 
                        bank fintech score for each year.  
                        The seven categories are: Mobile banking, Digital lending, Payment, Investment services, Open Banking, Cybersecurity, 
                        Business operations.  
                        Note that the data relative to this variable was manually collected from the bank's annual reports.**
                        ''')
        elif sel_var == 'DUMMY':
                st.write(r'''
                        - **The variable :green[DUMMY] takes value 1 during 2020 and 2021, and 0 otherwise. This variables is used in order
                        to capture the effect of the pandemic on the relation between the development of fintech serivces and the banks 
                        profitability.**
                        ''')
        elif sel_var == 'BS':
                st.write(r'''
                        - **The variable :green[BS] (Board Size) represents the number of members in the board of directors.**
                        ''')
        elif sel_var == 'ID':
                st.write(r'''
                        - **The variable :green[ID] (Indipendent members) represents the number of the independent member in the board of
                        directors.**
                        ''')
        elif sel_var == 'LSIZE':
                st.write(r'''
                        - **The variable :green[LS] (Log Size) is the natural logarithm of total assets, it's used as proxy of bank's size.**  
                       ''')
        elif sel_var == 'CAP':
                st.write(r'''
                        - **The variable :green[CAP] (Capital Ratio) is a financial ratio that measures the bank's risk exposure and its ability
                        to manage losses. It's a variable calculated by dividing the bank's equity by its total assets:**  
                        $$
                        \text{CAP} = \frac{\text{Equity}}{\text{Total Assets}}
                        $$''')
        elif sel_var == 'LOAN':
                st.write(r'''
                        - **The variable :green[LOAN] (Loan ratio) is a financial ratio that measures the weight of loans on the bank's 
                        profitability. It's a variable calculated by dividing the bank's total loans by its total assets:**  
                        $$
                        \text{LOAN} = \frac{\text{Total Loans}}{\text{Total Assets}}
                        $$''')
        elif sel_var == 'LLP':
                st.write(r'''
                        - **The variable :green[LLP] (Loan Loss Provisions) is a financial ratio used as credit risk measure that quantify
                        the asset's quality of the bank. It's a variable calculated by dividing the bank's loan loss provisions by its 
                        total loans:**  
                        $$
                        \text{LLP} = \frac{\text{Loan Loss Provisions}}{\text{Total Loans}}
                        $$''')
        elif sel_var == 'NONIN':
                st.write(r'''
                        - **The variable :green[NONIN] (Non-Interest Income) is a financial ratio that measures income diversification.
                        It's a variable calculated by dividing the bank's non-interest income by its total income:**  
                        $$
                        \text{NONIN} = \frac{\text{Non-Interst Income}}{\text{Total Income}}
                        $$''')
        elif sel_var == 'GDP':
                st.write(r'''
                        - **The variable :green[GDP] represents the Gross Domestic Product growth rate.**
                        ''')
        elif sel_var == 'INF':
                st.write(r'''
                        - **The variable :green[INF] represents the inflation rate.**
                        ''')
        elif sel_var == 'Z_SCORE':
                st.write(r'''
                        - **The variable :green[Z-Score] is used as proxy to measure the probability of default of the bank. It's a variable
                        calculated by dividing the sum between the capital ratio and return on assets by the standard deviation of 
                        the latter:**  
                        $$
                        \text{Z-SCORE} = \frac{\text{CAP+ROA}}{\sigma\text{(ROA)}}
                        $$''')
                        
selectvar()

####### MODEL #######
st.write(
        '''
        ----
        ## Econometric Model
        The model developed to describe the effect of fintech services on the bank's performance is a regression fixed effects model, 
        where the dependent variables are ROA and ROE.
        ''')
st.latex(
        r'''
        \begin{array}{lcl}
        \text{ROA19}_{it}=\alpha_i+\beta_1FS+\beta_2BS_{it}+\beta_3ID_{it}+\beta_4LSIZE_{it}+\beta_5CAP_{it} & &
        \text{ROE19}_{it}=\alpha_i+\beta_1FS+\beta_2BS_{it}+\beta_3ID_{it}+\beta_4LSIZE_{it}+\beta_5CAP_{it}\\
        +\beta_6LOAN_{it}+\beta_7LLP_{it}+\beta_8NONIN_{it}+\beta_{9}GDP_{it} & &
        +\beta_6LOAN_{it}+\beta_7LLP_{it}+\beta_8NONIN_{it}+\beta_{9}GDP_{it}\\
        +\beta_{10}INF_{it}+\beta_{11}Z\_SCORE_{it}+u_{it} & &
        +\beta_{10}INF_{it}+\beta_{11}Z\_SCORE_{it}+u_{it}
        \end{array}
        ''')
st.write(
        '''
        In second analysis, from 2020 to 2021, in the model is included a binary variable, that can control for the pandemic factor and let us know
        the impact of the COVID-19 on the relation between the development of fintech serivces and the banks profitability.
        ''')
st.latex(
        r'''
        \begin{array}{lcl}
        \text{ROA21}_{it}=\alpha_i+\beta_1FS+\beta_2DUMMY+\beta_3BS_{it}+\beta_4ID_{it}+\beta_5LSIZE_{it} & &
        \text{ROE21}_{it}=\alpha_i+\beta_1FS+\beta_2DUMMY+\beta_3BS_{it}+\beta_4ID_{it}+\beta_5LSIZE_{it}\\
        +\beta_6CAP_{it}+\beta_7LOAN_{it}+\beta_8LLP_{it}+\beta_9NONIN_{it} & &
        +\beta_6CAP_{it}+\beta_7LOAN_{it}+\beta_8LLP_{it}+\beta_9NONIN_{it}\\
        +\beta_{10}GDP_{it}+\beta_{11}INF_{it}+\beta_{12}Z\_SCORE_{it}+u_{it} & &
        +\beta_{10}GDP_{it}+\beta_{11}INF_{it}+\beta_{12}Z\_SCORE_{it}+u_{it}
        \end{array}
        ''')

####### RESULTS #######
st.write(
        '''
        ---
        ## Empiric Results
        ''')
st.write(
        '''
        ### Descriptive Analysis
        #### Mean, Standard Deviation, Percentile
        ''')
st.table(descriptive)

st.write(
        '''
        #### Correlation Matrix (Pearson)
        ''')
st.table(corr)

st.markdown(
        '''
        ### Tests
        The choice of using a regression model with entity effects instead of a model with random effects was tested through the Hausman Test.
        Also, was tested the presence of heteroskedasticity and serial correlation.\\
        The tests results are provided in the following table:
        <style>
                table {
                        margin:auto;
                        width: 90%;
                }
                .testcolor{
                        background-color: #14872d;
                }
        </style>
        <div>
                <table>
                        <tr>
                                <th></th>
                                <th class='testcolor'>ROA19</th>
                                <th class='testcolor'>ROA21</th>
                                <th class='testcolor'>ROE19</th>
                                <th class='testcolor'>ROE21</th>
                        </tr>
                                <td>Test</td>
                                <td>(p-value)</td>
                                <td>(p-value)</td>
                                <td>(p-value)</td>
                                <td>(p-value)</td>
                        <tr>
                        </tr>
                                <td>Hausman</td>
                                <td>0.0002</td>
                                <td>0.0000</td>
                                <td>0.0450</td>
                                <td>0.0000</td>
                        <tr>
                                <td>Heteroskedasticity</td>
                                <td>0.0001</td>
                                <td>0.0001</td>
                                <td>0.0001</td>
                                <td>0.0001</td>
                        </tr>
                        <tr>
                                <td>Serial Correlation</td>
                                <td>0.2652</td>
                                <td>0.0545</td>
                                <td>0.0023</td>
                                <td>0.0030</td>
                        </tr>
                        <tr>
                        </tr>
                </table>
        </div>
        ''', unsafe_allow_html = True)

st.write(
        '''
        ### Regression Analysis  

        ''')

deps19 = ('ROA', 'ROE')
sel_deps19 = st.multiselect('Choose the dependent variable for the time period 2014-2019', deps19)
if sel_deps19 == ['ROA']:
        st.header('ROA')
        st.table(tableROA)
elif sel_deps19 ==  ['ROA', 'ROE']:
        col1, col2 = st.columns(2)
        col1.header('ROA')
        col1.table(tableROA19)
        col2.header('ROE')
        col2.table(tableROE19)
elif sel_deps19 == ['ROE', 'ROA']:
        col1, col2 = st.columns(2)
        col1.header('ROE')
        col1.table(tableROE19)
        col2.header('ROA')
        col2.table(tableROA19)
elif sel_deps19 == ['ROE']:
        st.header('ROE')
        st.table(tableROE19)

deps = ('ROA', 'ROE')
sel_deps = st.multiselect('Choose the dependent variable for the time period 2014-2021', deps, key='1')
if sel_deps == ['ROA']:
        st.header('ROA')
        st.table(tableROA)
elif sel_deps ==  ['ROA', 'ROE']:
        col1, col2 = st.columns(2)
        col1.header('ROA')
        col1.table(tableROA)
        col2.header('ROE')
        col2.table(tableROE)
elif sel_deps == ['ROE', 'ROA']:
        col1, col2 = st.columns(2)
        col1.header('ROE')
        col1.table(tableROE) 
        col2.header('ROA')
        col2.table(tableROA)
elif sel_deps == ['ROE']:
        st.header('ROE')
        st.table(tableROE)


####### Conclusion #######
st.write(
        '''
        ---
        ## Conclusion  
        The obtained results evidence a negative relationship between the development of fintech services and the banks profitability.
        A possible interpretation can derive from the fact that, since Italy is still in an inital stage of FinTech, the projects and 
        services carried out by the banks do not yet present the adequate conditions to be able to achieve positive cash flows, even 
        if the forecastsalready show starting from the next few years higher revenues. In fact, the fintech projects referred to in the 
        FS variable do have a long term horizon. The second part of the analysis carries out two main results. The first one is that the
        pandemic has led to a decrease on the banks profitability. The second result is given by the evidence according to which fintech 
        services developed by banks have a lower negative impact on banking performance compared to the results obtained in the first part
        the analysis. Therefore, we can suppose that the pandemic accelerated the digital transformation process,  enabling the FinTech
        sector to help traditional banks towards this transition.  
        Of these conclusions must be considered the limitation, due to the small sample of data used.
        ''')

####### Appendix #######
import base64
def show_pdf():
        with open('analysis.pdf',"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
st.write('''
        ---
        ## Appendix  
        For more details (in italian) open the analysis pdf.
        ''')
if st.button('Read PDF',key='33'):
                show_pdf()
st.button('Close PDF',key='34')
                    

