#                        *
#                       * *
#                      *****
#                     *     *
#                    * *   * *
#                   ***** *****
#                  *           *
#                 * *         * *
#                *****       *****
#               *     *     *     *
#              * *   * *   * *   * *
#             ***** ***** ***** *****
#            *                       *
#           * *                     * *
#          *****                   *****
#         *     *                 *     *
#        * *   * *               * *   * *
#       ***** *****             ***** *****
#      *           *           *           *
#     * *         * *         * *         * *
#    *****       *****       *****       *****
#   *     *     *     *     *     *     *     *
#  * *   * *   * *   * *   * *   * *   * *   * *
# ***** ***** ***** ***** ***** ***** ***** *****
#
# N = [3 * (2 ** k) for k in range(11)]
# print(N)
# # [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]


# 첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다. (3, 6, 12, 24, 48, ...) (k<=10)
#
# 첫째 줄부터 N번째 줄까지 별을 출력한다.
# 24

# for k in range(0, 5):
#     print(k, b)
# x = '그리고자 하는 삼각형의 크기와 위치에 대한 함수를 정의해 재귀적으로 문제를 해결해봅니다'
#
# original = ['--*---', '-*-*--', '*****-']
# def star(n):
#     for i in original:
#         print(i)
# b = 3 * (2 ** k)
#
# def star(n):
#     for i in original:
#         print(i*n)
#     if n>0:
#         star(*n)
