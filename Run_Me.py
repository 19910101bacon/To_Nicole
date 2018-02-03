# -*- coding: utf-8 -*-

##########################################################################
######################你的作業，把他填完才能執行哦！###########################
##########################################################################

# 這裡要放下面程式碼所使用的套件，那看別人寫的寫法大致有四種
#(1) import numpy
#(2) import numpy as np
#(3) from numpy import sum
#(4) from numpy import *      # 這個和 R 的 library 下法是等價的

# 四種差別是
#(1) 第一種的，後面的程式只要使用到 numpy 套件裡面的函數，都要這樣寫  numpy.sum   (有點像 dplyr::group_by)
#(2) 第二種的，後面的程式不需要打numpy，只要打np就好，後面的程式要寫  np.sum
#(3) 第三種，我只import sum 這個函數，好處是  後面都可以值些打  sum ，但缺點是 numpy這套件內的其他函數不能使用
#(4) 第四種，就是我可以在後面只打  sum ，不需要在前面打 numpy，而且引入了套件其他的函數

# ok 那你的作業就是：這下面的指令有使用2個套件，所以你的答案會有兩行，輸入正確，整個函數就可以執行摟

import os
import numpy as np

##########################################################################
##########################################################################

## 在os這個資料夾 下path.py 這個檔案中的 abspath 函數：可以幫你找到電腦中，你輸入的這個檔案的位置，存為Path
Path = os.path.abspath('Run_Me.py')
## chdir 這個函數是將現在的路徑導成 Run_Me.py那個資料夾，你把它當成 setwd()
os.chdir(Path[0:-10])

# 如果你要把 str 接起來的話，只要用 + 就好
a1 = 'https:' + '//drive.google.com/'  # 這樣的話就會變成 'https://drive.google.com/'

# 如果你是對 list 做 + 的話 ，好比 [2] + [5] 就會變成 [2, 5]，而不是 [25] 哦！
# 如果你今天有串文字，好比 ['I_love_Nicole']，你想要讓他從list變成str的話， ''.join()  這個方式我很常用，換句話說就是把 list 解掉
a2 = ''.join(  ['open?id=1u5m_zXz']  )  # join()裡面接的是個list哦

#介紹 numpy 套件（常用
# 在python 裡面，你想要做加法，可不能直接打 sum 哦，好比 sum([1,3,5])  這樣會跑出error，因為sum 是 numpy這個package裡面的指令
# 所以你要打 import numpy 接著下一行在打 numpy.sum([1,3,5])
# 但是你會發現下面怎麼只有 np.sum ，因為大多人在使用numpy這個套件，會很懶得把全名寫出來
# 所以會 import numpy as np ，這樣的話，以後只要打 np. 就好，不需要 numpy.
a3 = np.sum([1,3,5])

# 介紹pandas套件
# Dataframe 由 一堆 array 構成，這點要注意
# 我現在要來製作個 Dataframe (製作Dataframe 的方法很多，以下只是其中一個)
try:
    ##### 因為你可能沒有裝 pandas ，所以可能執行會有問題，所以用 try excep 除錯
    import pandas as pd
    # step1 先做個 dictionary
    d = {'col1':['a', 'e', 't', 'W', 'l'], 'col2':['A','o','T','1','a']}
    # step2 用 pandas 下面的DataFrame函數
    df = pd.DataFrame(data=d)
    # 你可以執行這個看看 print(df)
    # 我要取col1出來，那就是執行這樣  df['col1']

    # 現在我要用 for 迴圈把所有值列出來
    # step1 我比較懶，首先我先把所有 column 都串再一起
    df_list = df['col1'].tolist() + df['col2'].tolist()  # .tolist 是把串列強至轉換成list
    a4 = ''
    for i in range(len(df_list)):    # len 是看一個list有多少個元素，像這裡 len(df_list) = 10 , 那 range(10) 就是 0 ~ 9
        a4 +=  df_list[i]  # += 的意思就是 :   a4 = a4 + df_list[i]
except:
    a4 = 'aetWlAoT1a'
# 下次再教你
# 空格 很重要
# 裝套件
# quit 很重要


#為什麼下面要有個 str 包住 a3 呢？ 因為 a3是 integer ，要把他強制轉換成string
print('請上網輸入 : ' + a1 + a2 + str(a3) + a4 + 'VNnmcjMgT0H88Q')




##### 作業的 Ans   (三個點刮起來的 中間內容不會執行)
'''
import os
import numpy as np
import pandas as pd
'''
