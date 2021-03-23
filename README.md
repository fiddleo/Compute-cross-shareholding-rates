# Compute-cross-shareholding-rates
## Defenition and Demand

"**Cross holding** is a situation in which a publicly-traded corporation owns stock in another publicly-traded company." (Will Kenton, 2021)

For example, there are four companies named `A1`, `A2`, `A3 ` and  `A4`. Direct shareholding ratios between companies are presented as below.

| company | controlled company | rate |
| ------- | ------------------ | ---- |
| A1      | A2                 | 0.1  |
| A2      | A3                 | 0.2  |
| A3      | A4                 | 0.7  |
| A4      | A1                 | 0.1  |

* Explanation: Company `A1` holds 10% of Company `A2`'s shares; 
  * Company `A2` holds 20% of Company `A3`'s shares; 
  * Company `A3` holds 70% of Company `A4`'s shares; 
  * Company `A4` holds 10% of Company `A1`'s shares;

**Demand**: I want to calculate the actual shareholding ratio (total shareholding) between two companies.

- For example,  how many shares Company `A1` holds in Company `A4` 

****

Reference: Will Kenton. (2021, January 29). Cross Holding. Retrieved from https://www.investopedia.com/terms/c/cross-holding.asp



## Principles of Mathematics

Suppose there are `n` companies named `A1` , `A2`,... , `An`. Cross-shareholding relationships exist between each other. The direct shareholding ratio of A to B is recorded as <a href="https://www.codecogs.com/eqnedit.php?latex=a_{ij}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{ij}" title="a_{ij}" /></a>.

$A$ is a **direct shareholding ratio matrix**. The diagonal elements of matrix A are all 0, which means that the direct shareholding ratio of the company to itself is 0.

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{A}=\left[\begin{array}{cccc}&space;a_{11}&space;&&space;a_{12}&space;&&space;\cdots&space;&&space;a_{1&space;n}&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;a_{n&space;1}&space;&&space;a_{n&space;2}&space;&&space;\cdots&space;&&space;a_{n&space;n}&space;\end{array}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathrm{A}=\left[\begin{array}{cccc}&space;a_{11}&space;&&space;a_{12}&space;&&space;\cdots&space;&&space;a_{1&space;n}&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;a_{n&space;1}&space;&&space;a_{n&space;2}&space;&&space;\cdots&space;&&space;a_{n&space;n}&space;\end{array}\right]" title="\mathrm{A}=\left[\begin{array}{cccc} a_{11} & a_{12} & \cdots & a_{1 n} \\ \cdots & \cdots & \cdots & \cdots \\ \cdots & \cdots & \cdots & \cdots \\ a_{n 1} & a_{n 2} & \cdots & a_{n n} \end{array}\right]" /></a>


For the aforementioned example,

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{A}=\left[\begin{array}{cccc}0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0\end{array}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathrm{A}=\left[\begin{array}{cccc}0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0\end{array}\right]" title="\mathrm{A}=\left[\begin{array}{cccc}0 & 0.1 & 0 & 0 \\ 0 & 0 & 0.2 & 0 \\ 0 & 0 & 0 & 0.7 \\ 0.1 & 0 & 0 & 0\end{array}\right]" /></a>

- <a href="https://www.codecogs.com/eqnedit.php?latex=a_{12}=0.1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{12}=0.1" title="a_{12}=0.1" /></a> means that Company `A1` holds 10% of Company `A2`'s shares; 
- <a href="https://www.codecogs.com/eqnedit.php?latex=a_{23}=0.2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{23}=0.2" title="a_{23}=0.2" /></a>;  
- <a href="https://www.codecogs.com/eqnedit.php?latex=a_{34}=0.7" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{34}=0.7" title="a_{34}=0.7" /></a>;  
- <a href="https://www.codecogs.com/eqnedit.php?latex=a_{41}=0.1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{41}=0.1" title="a_{41}=0.1" /></a>.

We can calculate the **total shareholding matrix** C based on matrix A.

- <a href="https://www.codecogs.com/eqnedit.php?latex=C=A&space;\times(I-A)^{-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=A&space;\times(I-A)^{-1}" title="C=A \times(I-A)^{-1}" /></a>
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{C}=\left[\begin{array}{cccc}\mathrm{c}_{11}&space;&&space;\mathrm{c}_{12}&space;&&space;\cdots&space;&&space;\mathrm{c}_{1&space;\mathrm{n}}&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;c_{n&space;1}&space;&&space;c_{n&space;2}&space;&&space;\cdots&space;&&space;c_{n&space;n}\end{array}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathrm{C}=\left[\begin{array}{cccc}\mathrm{c}_{11}&space;&&space;\mathrm{c}_{12}&space;&&space;\cdots&space;&&space;\mathrm{c}_{1&space;\mathrm{n}}&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;\\&space;c_{n&space;1}&space;&&space;c_{n&space;2}&space;&&space;\cdots&space;&&space;c_{n&space;n}\end{array}\right]" title="\mathrm{C}=\left[\begin{array}{cccc}\mathrm{c}_{11} & \mathrm{c}_{12} & \cdots & \mathrm{c}_{1 \mathrm{n}} \\ \cdots & \cdots & \cdots & \cdots \\ \cdots & \cdots & \cdots & \cdots \\ c_{n 1} & c_{n 2} & \cdots & c_{n n}\end{array}\right]" /></a>
  - I is an identity matrix  (n × n square matrix with ones on the main diagonal and zeros elsewhere)
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\mathrm{I}=\left[\begin{array}{cccc}1&space;&&space;0&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1\end{array}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathrm{I}=\left[\begin{array}{cccc}1&space;&&space;0&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1\end{array}\right]" title="\mathrm{I}=\left[\begin{array}{cccc}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{array}\right]" /></a>

For the aforementioned example,

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}&space;C&space;&=A&space;\times(I-A)^{-1}&space;\\&space;&=\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\times\left(\left[\begin{array}{cccc}&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;\end{array}\right]-\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]\right)^{-1}&space;\\&space;&=\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\times\left[\begin{array}{ccccc}&space;1.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;1.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;1.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;1.00140196&space;\end{array}\right]&space;\\\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{aligned}&space;C&space;&=A&space;\times(I-A)^{-1}&space;\\&space;&=\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\times\left(\left[\begin{array}{cccc}&space;1&space;&&space;0&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;1&space;\end{array}\right]-\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]\right)^{-1}&space;\\&space;&=\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\times\left[\begin{array}{ccccc}&space;1.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;1.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;1.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;1.00140196&space;\end{array}\right]&space;\\\end{aligned}" title="\begin{aligned} C &=A \times(I-A)^{-1} \\ &=\left[\begin{array}{cccc} 0 & 0.1 & 0 & 0 \\ 0 & 0 & 0.2 & 0 \\ 0 & 0 & 0 & 0.7 \\ 0.1 & 0 & 0 & 0 \end{array}\right] \times\left(\left[\begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right]-\left[\begin{array}{cccc} 0 & 0.1 & 0 & 0 \\ 0 & 0 & 0.2 & 0 \\ 0 & 0 & 0 & 0.7 \\ 0.1 & 0 & 0 & 0 \end{array}\right]\right)^{-1} \\ &=\left[\begin{array}{cccc} 0 & 0.1 & 0 & 0 \\ 0 & 0 & 0.2 & 0 \\ 0 & 0 & 0 & 0.7 \\ 0.1 & 0 & 0 & 0 \end{array}\right] \times\left[\begin{array}{ccccc} 1.00140196 & 0.1001402 & 0.02002804 & 0.01401963 \\ 0.01401963 & 1.00140196 & 0.20028039 & 0.14019627 \\ 0.07009814 & 0.00700981 & 1.00140196 & 0.70098137 \\ 0.1001402 & 0.01001402 & 0.0020028 & 1.00140196 \end{array}\right] \\\end{aligned}" /></a>

  <a href="https://www.codecogs.com/eqnedit.php?latex==\left[\begin{array}{cccc}&space;0.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=\left[\begin{array}{cccc}&space;0.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]" title="=\left[\begin{array}{cccc} 0.00140196 & 0.1001402 & 0.02002804 & 0.01401963 \\ 0.01401963 & 0.00140196 & 0.20028039 & 0.14019627 \\ 0.07009814 & 0.00700981 & 0.00140196 & 0.70098137 \\ 0.1001402 & 0.01001402 & 0.0020028 & 0.00140196 \end{array}\right]" /></a>

- <a href="https://www.codecogs.com/eqnedit.php?latex=c_{11}=0.00140196" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{11}=0.00140196" title="c_{11}=0.00140196" /></a> means that Company `A1` holds about 0.14% of its own shares; 
- <a href="https://www.codecogs.com/eqnedit.php?latex=c_{12}=0.1001402" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{12}=0.1001402" title="c_{12}=0.1001402" /></a> means that Company `A1` holds 10.01402% of Company `A2`'s shares; 

We also can calculate the **indirect shareholding matrix** B

- B=C-A

For the aforementioned example,
<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}&space;B&space;&=C-A&space;\\&space;&=\left[\begin{array}{llll}&space;0.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]-\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\\&space;&=\left[\begin{array}{cccc}&space;0.00140196&space;&&space;0.0001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.00028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.00098137&space;\\&space;0.0001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]&space;\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{aligned}&space;B&space;&=C-A&space;\\&space;&=\left[\begin{array}{llll}&space;0.00140196&space;&&space;0.1001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.20028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.70098137&space;\\&space;0.1001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]-\left[\begin{array}{cccc}&space;0&space;&&space;0.1&space;&&space;0&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0.2&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;0&space;&&space;0.7&space;\\&space;0.1&space;&&space;0&space;&&space;0&space;&&space;0&space;\end{array}\right]&space;\\&space;&=\left[\begin{array}{cccc}&space;0.00140196&space;&&space;0.0001402&space;&&space;0.02002804&space;&&space;0.01401963&space;\\&space;0.01401963&space;&&space;0.00140196&space;&&space;0.00028039&space;&&space;0.14019627&space;\\&space;0.07009814&space;&&space;0.00700981&space;&&space;0.00140196&space;&&space;0.00098137&space;\\&space;0.0001402&space;&&space;0.01001402&space;&&space;0.0020028&space;&&space;0.00140196&space;\end{array}\right]&space;\end{aligned}" title="\begin{aligned} B &=C-A \\ &=\left[\begin{array}{llll} 0.00140196 & 0.1001402 & 0.02002804 & 0.01401963 \\ 0.01401963 & 0.00140196 & 0.20028039 & 0.14019627 \\ 0.07009814 & 0.00700981 & 0.00140196 & 0.70098137 \\ 0.1001402 & 0.01001402 & 0.0020028 & 0.00140196 \end{array}\right]-\left[\begin{array}{cccc} 0 & 0.1 & 0 & 0 \\ 0 & 0 & 0.2 & 0 \\ 0 & 0 & 0 & 0.7 \\ 0.1 & 0 & 0 & 0 \end{array}\right] \\ &=\left[\begin{array}{cccc} 0.00140196 & 0.0001402 & 0.02002804 & 0.01401963 \\ 0.01401963 & 0.00140196 & 0.00028039 & 0.14019627 \\ 0.07009814 & 0.00700981 & 0.00140196 & 0.00098137 \\ 0.0001402 & 0.01001402 & 0.0020028 & 0.00140196 \end{array}\right] \end{aligned}" /></a>

- The explanations for matrix B are the same as matrix A and matrix C

****

Reference:  万立全.(2009).交叉持股下公司间持股比例的计算. *财会月刊*(22),49. doi:10.19641/j.cnki.42-1290/f.2009.22.032.


## Code

```python
import os
import numpy as np 
import pandas as pd 

def load_data(file_name):
    '''load data from excel'''
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here ,os.pardir))
    file_path = os.path.join(input_dir, file_name + ".xlsx")
    df = pd.read_excel(file_path)
    return df
ctrlrate = load_data('company_ctrlrate') # direct shareholding ratio dataframe

comp_names = list({comp_name for row in ctrlrate.iloc[:,[0,1]].values for comp_name in row}) # 获取控股公司和被控股公司名，集合去重，转list
      # company name
comp_id = [i+1 for i in range(len(comp_names))]  # company id
comp_dic = {'id':comp_id, 'company_name':sorted(comp_names)}
comp_df = pd.DataFrame(comp_dic)                 # dataframe of all the companies
n = len(comp_df)
matrix = np.zeros((n,n))   # 有n家公司就创建 (n,n)的矩阵
                           # if there are n companies, create (n,n) matrix

comps = list(comp_df['company_name'])
for row in range(len(comps)):
    for col in range(len(comps)):
        value = list(ctrlrate.loc[(ctrlrate['company']==comps[row])&(ctrlrate['controlled_company']==comps[col]),'rate'])    
        if len(value)>0:
            matrix[row,col]=value[0]      

A = matrix    # 直接持股比例矩阵 direct shareholding ratio matrix
I = np.eye(n) # 对角线为1的矩阵  identity matrix
C = np.dot(A, np.linalg.inv(I-A) ) 
              # 全部控股矩阵 total shareholding matrix; C = A*(I-A)^{-1}
B = (C-A)     # 间接控股矩阵 indirect shareholding matrix


# 全部控股df; total shareholding dataframe
dic = {'company':[],'controlled_company':[],'total_shareholding_ratio':[]}
for row in range(len(comps)):
    for col in range(len(comps)):       
        company_name = comps[row]
        controlled_company_name = comps[col] 
        ratio = C[row,col]
        dic['company'].append(company_name)
        dic['controlled_company'].append(controlled_company_name)
        dic['total_shareholding_ratio'].append(ratio)
df = pd.DataFrame(dic) # total shareholding dataframe


# 间接控股df; indirect shareholding dataframe
indirect_dic = {'company':[],'controlled_company':[],'indirect_shareholding_ratio':[]}
for row in range(len(comps)):
    for col in range(len(comps)):       
        comp_name = comps[row]
        ctrled_company_name = comps[col] 
        indirect_ratio = B[row,col]
        indirect_dic['company'].append(comp_name)
        indirect_dic['controlled_company'].append(ctrled_company_name)
        indirect_dic['indirect_shareholding_ratio'].append(indirect_ratio)
indirect_df = pd.DataFrame(indirect_dic) # indirect shareholding dataframe


print('total shareholding dataframe',df)
print('indirect shareholding dataframe',indirect_df)
```



## Run the code step by step

![](https://i.loli.net/2021/03/18/fz1JlqcREknSmFW.png)

![](https://i.loli.net/2021/03/18/1hzjIqYmXxAaSb9.png)



## Merits of this method

- You can add more companies and rates in  `company_ctrlrate` excel file and python will help you calculate all the actual shareholding rates (the actual shareholding rates) and indirect shareholding rates between every two companies.
- Python is handy for calculating complex cross-shareholdings.
