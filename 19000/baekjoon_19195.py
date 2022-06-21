MOD = 7340033
def resize(arr, t):
    if t <= len(arr):
        return arr[:t]
    else:
        return arr + [0 for _ in range(t - len(arr))]
def multiply(v, w, rec):
    m = len(v)
    t = [0 for _ in range(m * 2)]
    for i in range(m):
        for j in range(m):
            t[i + j] += v[i] * w[j] % MOD
            if t[i + j] >= MOD:
                t[i + j] -= MOD
    for i in range(m, 2 * m)[::-1]:
        for j in range(1, m + 1):
            t[i - j] += t[i] * rec[j - 1] % MOD
            if t[i - j] >= MOD:
                t[i - j] -= MOD
    t = resize(t, m)
    return t
def berlekamp_massey(x):
    ls, cur = [], []
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t += x[i - j - 1] * cur[j]
            t %= MOD
        if (t - x[i]) % MOD == 0:
            continue
        if not cur:
            cur = resize(cur, i + 1)
            lf = i
            ld = (t - x[i]) % MOD
            continue
        k = -(x[i] - t) * pow(ld, MOD - 2, MOD) % MOD
        c = [0 for _ in range(i - lf - 1)] + [k]
        for j in ls:
            c.append(-j * k % MOD)
        if len(c) < len(cur):
            c = resize(c, len(cur))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % MOD
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % MOD
        cur = c[:]
    for i in range(len(cur)):
        cur[i] = (cur[i] % MOD + MOD) % MOD
    return cur
def get_nth(rec, numlist, n):
    m = len(rec)
    s = [1] + [0 for _ in range(m - 1)]
    t = [0, 1] + [0 for _ in range(m - 2)] if m != 1 else [rec[0]] + [0 for _ in range(m - 1)]
    while n:
        if n & 1:
            s = multiply(s, t, rec)
        t = multiply(t, t, rec)
        n >>= 1
    result = 0
    for i in range(m):
        result += s[i] * numlist[i] % MOD
    return result % MOD
def guess_nth_term(x, n):
    return x[n] if n < len(x) else 0 if not (v := berlekamp_massey(x)) else get_nth(v, x, n)
print(guess_nth_term([1, 2, 4, 4, 6, 10, 12, 14, 22, 26, 30, 44, 56, 70, 98, 130, 162, 216, 292, 358, 470, 628, 792, 1050, 1384, 1788, 2334, 3072, 3974, 5162, 6784, 8786, 11420, 14992, 19484, 25388, 33160, 43262, 56252, 73392, 95798, 124496, 162556, 212048, 275976, 360154, 469694, 611844, 797628, 1040344, 1355550, 1766402, 2304368, 3002354, 3913802, 5103798, 6651808, 1330929, 3964467, 56364, 4526934, 3020079, 3283660, 5845937, 4089463, 6249217, 6173168, 5434618, 6035817, 3277472, 599541, 2502130, 101659, 1046904, 615205, 4310505, 7073937, 1528843, 1573423, 628109, 3338517, 7141678, 6639170, 7199721, 2508559, 6983719, 3226808, 1362909, 4057445, 5216401, 4789473, 7148607, 3490252, 3859839, 3919928, 4410603, 1774464, 5030371, 3213868, 3673656, 2253480, 162153, 6967672, 6212357, 1488891, 5272969, 2288129, 3900589, 6122846, 6177603, 475903, 151346, 4687899, 1154734, 4168110, 1744680, 1925769, 3198859, 1886183, 702652, 4959058, 6769965, 4832688, 6752128, 5192022, 872961, 2974929, 4528640, 4768052, 929662, 5895668, 7181370, 6213930, 7284455, 594448, 3091509, 5305389, 2707419, 3941867, 1121753, 845827, 3309438, 595600, 781040, 946746, 13034, 2718932, 7085679, 3266476, 5093050, 2885519, 857478, 1824149, 1260691, 7159165, 4673614, 6783666, 3610236, 6096057, 2407175, 4363867, 1045797, 5634741, 1318874, 2419385, 5566960, 2819845, 1796225, 4713192, 6402160, 4166441, 7316367, 784543, 804460, 6056725, 3566002, 614866, 2966829, 4200759, 6854749, 1255022, 5313359, 2068175, 4568467, 3205817, 7247886, 1465426, 6774868, 4232114, 880160, 915057, 2676981, 2099293, 6754336, 81171, 6249465, 2149619, 1956981, 5209736, 6104526, 1338219, 4813766, 6792238, 2331866, 575940, 3317255, 6298367, 2446752, 6992848, 3610017, 84047, 565196, 6348443, 2260995, 6299457, 2212791, 4491759, 5328705, 4512429, 5627861, 2856703, 365802, 3600986, 122013, 4066515, 7156238, 4011216, 6406274, 2259272, 5956744, 5437532, 935425, 3623786, 1544379, 2877350, 6534755, 5832885, 92285, 4464208, 521753, 6348728, 46324, 3621726, 2939887, 6438183, 5894808, 3263333, 4759589, 3286518, 5159126, 1391036, 1350878, 399877, 6593520, 4143141, 3724155, 5761110, 1798424, 3293002, 4100335, 4532028, 6561362, 2750870, 4607339, 21291, 1045121, 1406340, 2154712, 2772527, 5443968, 1661113, 7278227, 4896755, 2912920, 2248374, 193763, 4238085, 467750, 6617240, 7262374, 636881, 542871, 827084, 4875825, 3203478, 599091, 1860856, 1803665, 233912, 588503, 4546309, 4529638, 2532515, 2857468, 1237101, 976927, 3267668, 7218217, 5509725, 1183105, 6834426, 560869, 2998729, 6608720, 6998366, 2339459, 3581220, 3841063, 1324953, 3649827, 1973586, 6395459, 1203683, 241155, 3490831, 4860503, 1775618, 3686373, 6100987, 7154381, 7072633, 5523002, 4599271, 5768615, 3721534, 5356898, 5016735, 235450, 3176023, 4773021, 4113079, 932700, 1580313, 4897601, 2852, 5958251, 3492918, 1490677, 4718169, 2675919, 396745, 4683503, 6377758, 5860516, 2089945, 4402011, 4421560, 6375023, 3019800, 2126709, 4131791, 3524017, 2823644, 2099673, 1985318, 5326275, 3605873, 4075817, 1751333, 5628472, 3881240, 3930886, 111846, 6439736, 749429, 4179309, 2353009, 7087033, 163239, 559695, 5538528, 497387, 3614649, 2002153, 1992716, 3483704, 1883604, 6447676, 7188486, 2231935, 6581603, 4190327, 3631067, 5452702, 4468896, 846626, 3409564, 148962, 2838706, 1868925, 1325853, 4842273, 553185, 6508043, 2377534, 4037902, 7193526, 4166210, 195558, 2898070, 3274123, 1246718, 4888445, 5874959, 4340272, 1458939, 3926500, 5704184, 2041581, 4495253, 5297666, 222261, 4472298, 2727307, 122132, 1505314, 5133667, 3099151, 2560544, 2470599, 2005536, 6282048, 505328, 7024970, 46638, 416713, 2869409, 6043900, 1506710, 728571, 5497854, 5797102, 579809, 4147867, 136614, 3817071, 288925, 1212310, 5262277, 6297642, 5909884, 1772015, 6258873, 150946, 5537266, 6832868, 6937997, 6203252, 4163885, 5543863, 2767535, 666574, 4737712, 1806200, 2697812, 5376164, 76860, 3737392, 5506589, 6238688, 4655489, 6828721, 6469344, 6427563, 1825701, 4999328, 3650759, 352586, 5849724, 3431108, 3482981, 6725764, 4638783, 5181185, 6365852, 4845481, 3385589, 146943, 6037649, 664226, 3899568, 6444785, 5045094, 6274560, 6948149, 5743742, 4653664, 2773649, 2474880, 2481311, 4093780, 6823136, 1875529, 1979171, 6814465, 512272, 750986, 3528802, 4045452, 3780344, 2631447, 6991591, 4500817, 6805990, 5894331, 1812684, 3598567, 1089100, 2699547, 5293309, 7282801, 4332624, 2337438, 6227966, 6911749, 1973198, 5727335, 6651979, 3532755, 494623, 1737538, 7028223, 3782586, 5227290, 602110, 5852380, 1354314, 2033574, 3849405, 2381068, 4614298, 2813078, 1728445, 4195071, 5265246, 3862275, 3230928, 6139546, 7307291, 3313700, 5690860, 2601810, 4204569, 1615786, 637597, 4101006, 2054938, 2362686, 2404667, 1789198, 6936768, 7114144, 5461472, 2986171, 781228, 2204008, 2756712, 5562005, 6909550, 3579486, 705180, 1248237, 6626610, 2798887, 1364824, 1728668, 2524441, 413734, 5310665, 716396, 1851575, 1180839, 1515544, 111183, 1496470, 3034047, 866495, 5150143, 2788905, 2396334, 3654635, 3406163, 991577, 2744608, 5904411, 390038, 880580, 2647055, 2141259, 4618614, 1579357, 6953379, 3553251, 6359262, 5204505, 7294141, 6089575, 6765513, 2065808, 1541962, 3285082, 525373, 3405093, 3101593, 4463980, 156872, 755494, 7304747, 7186217, 3641732, 6375005, 2397687, 1658402, 11388, 3219180, 890331, 4843378, 5842894, 5446851, 1173665, 2415429, 6988441, 2360928, 4086737, 6880588, 5713663, 5008639, 1690779, 2050882, 7106214, 361381, 4063825, 2641256, 5592611, 5874334, 4214370, 2550585, 4523653, 7280900, 1247259, 6846516, 3000722, 5080701, 6705914, 4469035, 535874, 6146595, 4680873, 4057947, 5694949, 2803856, 4543240, 2012615, 37848, 964783, 5399455, 482740, 575912, 6136759, 5250427, 5839024, 5031314, 602786, 5592665, 4613128, 126431, 829787, 1019012, 6037230, 4734987, 3678450, 5735468, 1301530, 1822193, 4315722, 6644565, 2065824, 5703491, 3854920, 4960169, 6779227, 3682946, 7174971, 2636896, 3824626, 2212329, 5446937, 662603, 5504504, 4551896, 504244, 5948948, 6854789, 5072625, 804854, 153831, 1363386, 1048269, 6747895, 6775845, 2734879, 1382423, 6278006, 1620296, 4721792, 5514315, 2612751, 213237, 608062, 3226165, 1459787, 2200960, 3275737, 3937391, 2515056, 4850682, 5276697, 262728, 5344697, 4777736, 1824208, 1654577, 5609712, 3769046, 5467684, 4292735, 4312274, 4315544, 7242221, 6069596, 2172458, 2168794, 6693006, 3164540, 3094313, 5850170, 1474989, 3344301, 1890927, 5750989, 5295680, 5427662, 5454230, 1389321, 4298362, 156372, 5355846, 1778433, 2232441, 2775583, 4525879, 1922311, 7303703, 6254167, 2519132, 5007687, 392103, 3075107, 2820743, 1431156, 6062941, 6485872, 5474518, 1658760, 1157337, 6843928, 683458, 5293473, 5799255, 2921296, 1278526, 3636303, 3338423, 2906500, 1941565, 6695980, 1135302, 562859, 2066622, 4936283, 4547207, 2894817, 2914937, 1775845, 1389337, 1011774, 2799508, 2437235, 2426242, 6095357, 4185415, 3368686, 661868, 4201375, 6222372, 2278555, 2577318, 4368802, 4895588, 2202375, 4013025, 1767786, 1930000, 5037453, 777886, 6990645, 1567014, 1195014, 3323934, 358436, 4620131, 1912763, 149079, 4565163, 613306, 1123410, 6528308, 2990906, 6747464, 660372, 1807081, 3245190, 2299131, 1505860, 7208552, 1875011, 3451804, 5023513, 4921405, 1172014, 5533411, 1530148, 4331826, 1944636, 2049654, 4553356, 3368810, 541466, 2687321, 6582879, 3870204, 1587071, 1172596, 2022313, 1383809, 2441155, 2059563, 260041, 5818970, 35819, 1132895, 3382957, 5006251, 3306425, 4270552, 961373, 2558526, 1393540, 1843692, 4378701, 1802398, 5063661, 5493488, 205720, 6192824, 5182296, 2412342, 3117353, 1277591, 847964, 6578198, 2191799, 128178, 1234403, 6071210, 5092457, 5027130, 3998894, 759202, 2557146, 2721283, 27687, 2697892, 2076965, 1552963, 5607306, 964579, 3901217, 5109962, 3289400, 2748033, 5175433, 4909264, 3789210, 3647930, 2316339, 4109460, 4099984, 1133958, 1181939, 1317151, 6960796, 6903664, 6633872, 2739293, 1342514, 4294077, 3464120, 4431336, 6404851, 2501654, 3003836, 3614965, 3001270, 4125247, 5411781, 3278209, 1554246, 2569659, 3816938, 7220596, 7224885, 2339852, 5992345, 3996958, 1004381, 5387007, 248181, 3011544, 6634716, 7016453, 3691921, 3218785, 656008, 5040415, 1789823, 468348, 5241612, 2265819, 1241341, 5377255, 7239800, 5678170, 5040634, 3738866, 5143799, 3044414, 6664653, 6777916, 4516556, 4926488, 4165691, 2926757, 7284802, 2066681, 5219282, 1235648, 6074140, 7083761, 6574341, 2648907, 1711998, 4687043, 3105681, 4052767, 4148989, 1135070, 2665060, 5557061, 4125996, 54887, 4800540, 974348, 1985073, 3221216, 1238295, 2496363, 6996829, 4124294, 4521651, 4308518, 6206340, 3807818, 2909013, 6186534, 5556242, 7095293, 1026532, 5981712, 5739277, 2567857, 3921354, 4913927, 3355647, 5219849, 6137618, 6010328, 321982, 6801937, 5605103], int(input())))
