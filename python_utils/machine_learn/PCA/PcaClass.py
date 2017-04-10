# _*_ coding:utf-8 _*_
import numpy as np
from utils.FileUtil import get_line_lst
import matplotlib.pyplot as plt


class PcaClass(object):
    def __init__(self):
        pass

    def pca(self, arr_data):
        mean_value = np.mean(arr_data, axis=0)
        sub_mean_value = arr_data - mean_value
        cov_arr = np.cov(sub_mean_value, rowvar=0)  # note rowvar=0
        print cov_arr
        eig_val, eig_vec = np.linalg.eig(cov_arr)
        print eig_val
        print eig_vec
        eig_val_sort_idx = np.argsort(eig_val)
        print eig_val_sort_idx
        eig_vec_max = eig_vec[:, eig_val_sort_idx[:-(1 + 1):-1]]
        vec_transform = eig_vec_max
        print 'vec_transform', vec_transform
        # low_dim_data = sub_mean_value * vec_transform.T
        low_dim_data = np.dot(sub_mean_value, vec_transform)
        # recon_data = low_dim_data * vec_transform.T + mean_value
        recon_data = low_dim_data * vec_transform.T

        return sub_mean_value, low_dim_data, recon_data
        pass


def load_data():
    file = '../dataset/pca/pca_data.txt'
    lst_row = get_line_lst(file)

    arr_data = np.array([[float(item) for item in row.split()] for row in lst_row])

    return arr_data


def sub_mean_data(data):
    """
    use source data subtract it's mean value
    :param data: np array
    :return:
    """
    return data - np.mean(data, axis=0)


def plot_compare_data(src_data, sub_mean_data):
    """
    The comparing plot of src_data and the value
    which is generated by src_data subtract it's mean value
    :param src_data:
    :param sub_mean_data:
    :return:
    """
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(src_data[:, 0], src_data[:, 1], c='r')
    plt.title('source data')

    plt.subplot(212)
    plt.scatter(sub_mean_data[:, 0], sub_mean_data[:, 1], c='r')
    plt.title('sub_mean_data')
    plt.show()


def plot_src_data(data):
    # f1 = plt.figure(1)
    # plt.plot(data, 'ro')
    # mt = np.array([[1, 2], [2.6, 3.6]])
    # print data[:, 0], data[:, 0].shape
    # print data[:, 1], data[:, 1].shape
    # x = [1, 2]
    # y = [2.6, 3.6]
    # plt.scatter(x, y)
    # add c='r', or you will get error
    plt.scatter(data[:, 0], data[:, 1], c='r')
    # plt.scatter(data, 'ro')
    plt.show()


def plot_eigen_vec(data, eig_vec):
    # plt.scatter(data[:, 0], data[:, 1], c='b')
    # plt.plot([eig_vec[:, 0][0], 0], [eig_vec[:, 0][1], 0], color='red')
    print eig_vec
    print [eig_vec[:, 0][0], 0], [eig_vec[:, 0][1], 0]
    print [eig_vec[:, 1][0], 0], [eig_vec[:, 1][1], 0]
    # plt.plot([eig_vec[:, 1][0], 0], [eig_vec[:, 1][1], 0], color='red')

    plt.show()


def plot_ret_data(src_data, sub_mean_data, low_dim_data, recon_data):

    f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
    ax1.scatter(src_data[:, 0], src_data[:, 1], c='r')
    ax1.set_title('source data')

    ax2.scatter(sub_mean_data[:, 0], sub_mean_data[:, 1], c='b')
    ax2.set_title('sub_mean_data')

    ax3.scatter(low_dim_data[:, 0], np.zeros(low_dim_data.shape)[:, 0], c='r')
    ax3.set_title('low_dim_data')

    ax4.scatter(recon_data[:, 0], recon_data[:, 1], c='g')
    ax4.set_title('reconstruct data')
    plt.show()
    pass


def do_pca():
    data = load_data()
    pca = PcaClass()
    mean_value, low_dim_data, recon_data = pca.pca(data)
    plot_ret_data(data, mean_value, low_dim_data, recon_data)

if __name__ == '__main__':
    do_pca()
    # data = load_data()
    # mean_data = sub_mean_data(data)
    # plot_compare_data(data, mean_data)
    # cov = np.cov(mean_data[:, 0], mean_data[:, 1])
    # eig_val, eig_vec = np.linalg.eig(cov)
    # print eig_val, eig_vec

    # cov2 = np.cov(data[:, 0], data[:, 1])
    # eig_val2, eig_vec2 = np.linalg.eig(cov2)
    # print eig_val2, eig_vec2

    # plot_eigen_vec(mean_data, eig_vec)
    # mt = np.array([[3, -1], [-1, 3]])
    # plot_src_data(data)
    # pca = PcaClass()
    # pca.pca(data)
    pass