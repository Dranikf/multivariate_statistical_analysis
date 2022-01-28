import numpy as np
import pandas as pd

def fin_num_of_steps(P, R, n, full_info = False):
    # функция реализующую вычислительную процедуру из пункта 13.2
    # вернет лист из табличек соотвесвующих шагам
    # формирует аналогичиный решению на листике "вывод" при установлении агрумента full_info в состояние True
    # входные данные:
    # P - массив матриц переходных вероятностей (list  содержащий ряд np.matrix)
    # R - массив матриц выйгрышей (list содержащий ряд np.matrix)
    # n - число шагов для задачи

    result = []

    v = {};

    strat_count = P[0].shape[0]

    # на первом шаге значения функций как 0
    f = np.zeros(strat_count)

    for i,p in enumerate(P):
        v["v_" +str(i+1)] = np.diag(np.dot(P[i], np.transpose(R[i])))
    


    if full_info:
        v_df = pd.DataFrame(v)
        v_df.index = pd.RangeIndex(1,strat_count+1)
        print()
        print()
        print('средние выйгрыши для i го состояния (по строкам)')
        print('и для k-й стратерии (по столбцам)')
        print(v_df)


    # цикл переибрает периоды
    for i in range(n,0,-1):
        f_comp = {}

        # цикл перебирает статегии
        for j,p in enumerate(P):
            f_comp['k='+str(j+1)] = np.array(np.dot(p,f) + v['v_' + str(j+1)])[0,:]

        new_f = pd.DataFrame(f_comp).apply(max, axis = 1)
        f_index = pd.DataFrame(f_comp).apply(lambda x: list(x).index(max(x)) + 1, axis = 1)
        f_comp['f'] = new_f
        f_comp['статерия'] = f_index
        f_comp = pd.DataFrame(f_comp)
        result.append(f_comp)

        f = np.array(new_f)

        if full_info:
            print()
            print()
            print('шаг номер ' + str(i))
            print(f_comp)
    
    return result;

# Example1
#P1 = np.matrix([[0.2, 0.5, 0.3], [0, 0.5, 0.5],[0, 0, -1]])
#P2 = np.matrix([[0.3, 0.6, 0.1], [0.1, 0.6, 0.3],[0.05, 0.4, 0.55]])

#R1 = np.matrix([[7, 6, 3], [0, 5, 1], [0, 0, 1]])
#R2 = np.matrix([[6, 5, -1], [7, 4, 0], [6, 3, -2]])

#fin_num_of_steps([P1, P2], [R1, R2], 3, True)
#print(np.dot(P1[0,:], np.zeros(3)))


# Example2
P1 = np.matrix([[0.9, 0.1], [0.6, 0.4]]);
P2 = np.matrix([[0.7, 0.3], [0.2, 0.8]]);

R1 = np.matrix([[2, -1], [1, -3]]);
R2 = np.matrix([[4, 1], [2, -1]]);

fin_num_of_steps([P1, P2], [R1, R2], 3, True)
