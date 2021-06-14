from math import sqrt
import numpy as np

def eucl_metrics(x1,x2):

    #сумма кавартатов отклонений соовтествующих координат
    dif_sqare_sum = 0

    for i,x1i in enumerate(x1):
        dif_sqare_sum += (x1i - x2[i])**2

    return sqrt(dif_sqare_sum)
    

def functional5_7(data, metrics_computer = eucl_metrics, info = False):
    #data = [[cluster1],[cluster2], ...] cluster[i] = pandas.dataframe

    # сумма квадратов расстояний до центра
    sq_dist_sum = 0

    # перебираем данные кластеры
    for i,cluster in enumerate(data):
            clust_mean = cluster.mean()

            if info:
                print("cluster:" + str(i) + "==================================================")
                print(cluster)
                print("cluster mean:")
                print(clust_mean)


            for j in cluster.index:
                sq_dist_sum += metrics_computer(clust_mean, cluster.loc[j])**2
    
    return sq_dist_sum

def functional5_8(data, metrics_computer = eucl_metrics, info = False):
    #data = [[cluster1],[cluster2], ...] cluster[i] = pandas.dataframe

    # сумма квадратов попарных расстояний 
    sq_dist_sum = 0

    # перебираем данные кластеры
    for i,cluster in enumerate(data):

        size = len(cluster.index)

        if info:
            print("cluster:" + str(i) + "==================================================")
            print(cluster)

        # то для скольки объектов попарные дистанции мы уже вычислили

        for h,j in enumerate(cluster.index):
            for k in cluster.index[h+1:]:

                if info:
                    print("items " + str(j) + " and " + str(k) + "-----------")
                    print("item "+ str(j) + ":" + str(cluster.loc[j].values.tolist()))
                    print("item "+ str(k) + ":" + str(cluster.loc[k].values.tolist()))
                    print("distance: " + str(metrics_computer(cluster.loc[j], cluster.loc[k])))
                    
                sq_dist_sum += metrics_computer(cluster.loc[j], cluster.loc[k])**2

    
    return sq_dist_sum

def functional5_9(data, metrics_computer = eucl_metrics, info = False):
    #data = [[cluster1],[cluster2], ...] cluster[i] = pandas.dataframe
    
    sum_matrix = 0

    # перебираем данные кластеры
    for i,cluster in enumerate(data):
        
        cov_mat = np.cov(np.array(cluster).T, bias = True)

        if info:
            print("cluster:" + str(i) + "==================================================")
            print(cluster)
            print("covariation: ")
            print(cov_mat)

        s = len(cluster.index)
        sum_matrix = sum_matrix + cov_mat*s
    
    return np.linalg.det(sum_matrix)


def functional5_10(data, metrics_computer = eucl_metrics, info = False):
    #data = [[cluster1],[cluster2], ...] cluster[i] = pandas.dataframe
    
    result = 1

    # перебираем данные кластеры
    for i,cluster in enumerate(data):
        
        cov_mat = np.cov(np.array(cluster).T, bias = True)
        det = np.linalg.det(cov_mat)

        if info:
            print("cluster:" + str(i) + "==================================================")
            print(cluster)
            print("covariation: ")
            print(cov_mat)
            print("cov det:")
            print(det)

        s = len(cluster.index)
        result *= det**s
    
    return result