"""some camera data that we need to store somewhere
"""

import numpy as np

# We "pythonify" the conventions in the Tkačik et al paper, so R=0, G=1, B=2
BAYER_MATRICES = {
    "NIKON D90": np.array([[1, 2], [0, 1]]),
    "NIKON D70": np.array([[2, 1], [1, 0]]),
    }


# context, content, direction, size of grating
IMG_INFO = {
    'DSC_0080': ['monitor', '1 cyc/image', 'vertical', '256 pix'],
    'DSC_0081': ['monitor', '2 cyc/image', 'vertical', '256 pix'],
    'DSC_0082': ['monitor', '4 cyc/image', 'vertical', '256 pix'],
    'DSC_0083': ['monitor', '8 cyc/image', 'vertical', '256 pix'],
    'DSC_0084': ['monitor', '16 cyc/image', 'vertical', '256 pix'],
    'DSC_0085': ['monitor', '32 cyc/image', 'vertical', '256 pix'],
    'DSC_0086': ['monitor', '64 cyc/image', 'vertical', '256 pix'],
    'DSC_0087': ['monitor', '128 cyc/image', 'vertical', '256 pix'],
    'DSC_0088': ['monitor', 'blank', 'blank', '256 pix'],
    'DSC_0090': ['projector_1', '1 cyc/image', 'vertical', '256 pix'],
    'DSC_0091': ['projector_1', '2 cyc/image', 'vertical', '256 pix'],
    'DSC_0092': ['projector_1', '4 cyc/image', 'vertical', '256 pix'],
    'DSC_0093': ['projector_1', '8 cyc/image', 'vertical', '256 pix'],
    'DSC_0094': ['projector_1', '16 cyc/image', 'vertical', '256 pix'],
    'DSC_0095': ['projector_1', '32 cyc/image', 'vertical', '256 pix'],
    'DSC_0096': ['projector_1', '64 cyc/image', 'vertical', '256 pix'],
    'DSC_0097': ['projector_1', '128 cyc/image', 'vertical', '256 pix'],
    'DSC_0098': ['projector_1', '1 cyc/image', 'horizontal', '256 pix'],
    'DSC_0099': ['projector_1', '2 cyc/image', 'horizontal', '256 pix'],
    'DSC_0100': ['projector_1', '4 cyc/image', 'horizontal', '256 pix'],
    'DSC_0101': ['projector_1', '8 cyc/image', 'horizontal', '256 pix'],
    'DSC_0102': ['projector_1', '16 cyc/image', 'horizontal', '256 pix'],
    'DSC_0103': ['projector_1', '32 cyc/image', 'horizontal', '256 pix'],
    'DSC_0104': ['projector_1', '64 cyc/image', 'horizontal', '256 pix'],
    'DSC_0105': ['projector_1', '128 cyc/image', 'horizontal', '256 pix'],
    'DSC_0106': ['projector_1', 'blank', 'blank', '256 pix'],
    'DSC_0205': ['projector_2', '1 cyc/image', 'vertical', '256 pix'],
    'DSC_0206': ['projector_2', '2 cyc/image', 'vertical', '256 pix'],
    'DSC_0207': ['projector_2', '4 cyc/image', 'vertical', '256 pix'],
    'DSC_0208': ['projector_2', '8 cyc/image', 'vertical', '256 pix'],
    'DSC_0209': ['projector_2', '16 cyc/image', 'vertical', '256 pix'],
    'DSC_0210': ['projector_2', '32 cyc/image', 'vertical', '256 pix'],
    'DSC_0211': ['projector_2', '64 cyc/image', 'vertical', '256 pix'],
    'DSC_0212': ['projector_2', '128 cyc/image', 'vertical', '256 pix'],
    'DSC_0214': ['projector_2', '1 cyc/image', 'horizontal', '256 pix'],
    'DSC_0215': ['projector_2', '2 cyc/image', 'horizontal', '256 pix'],
    'DSC_0216': ['projector_2', '4 cyc/image', 'horizontal', '256 pix'],
    'DSC_0217': ['projector_2', '8 cyc/image', 'horizontal', '256 pix'],
    'DSC_0218': ['projector_2', '16 cyc/image', 'horizontal', '256 pix'],
    'DSC_0219': ['projector_2', '32 cyc/image', 'horizontal', '256 pix'],
    'DSC_0220': ['projector_2', '64 cyc/image', 'horizontal', '256 pix'],
    'DSC_0221': ['projector_2', '128 cyc/image', 'horizontal', '256 pix'],
    'DSC_0222': ['projector_2', 'blank', 'blank', '256 pix'],
    'DSC_0236': ['projector_3', '1 cyc/image', 'vertical', '256 pix'],
    'DSC_0237': ['projector_3', '2 cyc/image', 'vertical', '256 pix'],
    'DSC_0238': ['projector_3', '4 cyc/image', 'vertical', '256 pix'],
    'DSC_0239': ['projector_3', '8 cyc/image', 'vertical', '256 pix'],
    'DSC_0240': ['projector_3', '16 cyc/image', 'vertical', '256 pix'],
    'DSC_0241': ['projector_3', '32 cyc/image', 'vertical', '256 pix'],
    'DSC_0242': ['projector_3', '64 cyc/image', 'vertical', '256 pix'],
    'DSC_0243': ['projector_3', '128 cyc/image', 'vertical', '256 pix'],
    'DSC_0244': ['projector_3', '1 cyc/image', 'horizontal', '256 pix'],
    'DSC_0245': ['projector_3', '2 cyc/image', 'horizontal', '256 pix'],
    'DSC_0246': ['projector_3', '4 cyc/image', 'horizontal', '256 pix'],
    'DSC_0247': ['projector_3', '8 cyc/image', 'horizontal', '256 pix'],
    'DSC_0248': ['projector_3', '16 cyc/image', 'horizontal', '256 pix'],
    'DSC_0249': ['projector_3', '32 cyc/image', 'horizontal', '256 pix'],
    'DSC_0250': ['projector_3', '64 cyc/image', 'horizontal', '256 pix'],
    'DSC_0252': ['projector_3', '128 cyc/image', 'horizontal', '256 pix'],
    'DSC_0253': ['projector_3', 'blank', 'blank', '256 pix'],
    'DSC_0254': ['projector_zoomed_in', '64 cyc/image', 'vertical', '256 pix'],
    'DSC_0255': ['projector_zoomed_in', '128 cyc/image', 'vertical', '256 pix'],
    'DSC_0256': ['projector_zoomed_in', '64 cyc/image', 'horizontal', '256 pix'],
    'DSC_0257': ['projector_zoomed_in', '128 cyc/image', 'horizontal', '256 pix'],
    'DSC_0258': ['projector_zoomed_in', 'blank', 'blank', '256 pix'],
    'DSC_0259': ['projector_3', 0, 'log_polar', '1080 pix'],
    }

# the key specifies which image we're referring to and should be the filename as saved in the
# metadata dictionary (that is, the filename with no directory or extension). each value here is a
# dictionary defining the edges of the various circles for the different images. they must
# therefore have the following keys: 'square_ctr', 'grating_edge', 'white_edge', 'black_edge', and
# 'image_size'. The two numbers in each tuple are the pixels, as you can find using inkscape,
# etc. THIS SHOULD NOT BE USED DIRECTLY. Use the function `load_pts_dict`, because (in order to get
# the values here to correspond to the right image indices), we need to subtract the second number
# in each tuple from img.shape[0]

# annoyingly, image_size has the opposite order of numbers that the points have, because image_size
# must be compared to image.size (which returns the numbers as y, x) while the points should have
# the scatter-like order x, y -- I SHOULD PROBABLY CHANGE THIS
PTS_DICT = {"DSC_0080":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0081":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0082":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0083":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0084":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0085":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0086":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0087":
            {"square_ctr": (2148, 1456),
             "grating_edge": [(2071, 2149), (1441, 1593), (1856, 732), (2644, 2143), (2854, 1290),
                              (2586, 731), (1913, 736)],
             "white_edge": [(2200, 2506), (3206, 1347), (2145, 376), (1073, 1425)],
             "black_edge": [(3566, 1368), (709, 1539), (725, 2563), (3571, 66)],
             "image_size": (2868, 4310)},
            "DSC_0090":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0091":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0092":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0093":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0094":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0095":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0096":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0097":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0098":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0099":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0100":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0101":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0102":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0103":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0104":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0105":
            {"square_ctr": (2400, 1463),
             "grating_edge": [(2400, 2153), (2945, 2153), (3059, 1406), (3046, 849), (2413, 842)],
             "white_edge": [(2168, 2492), (3115, 2479), (3377, 1724), (3372, 726), (1863, 517),
                            (1417, 1588)],
             "black_edge": [(1084, 1957), (1095, 2736), (3717, 2060), (3710, 766)],
             "image_size": (2868, 4310)},
            "DSC_0205":
            {"square_ctr": (2157, 1452),
             "grating_edge": [(2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371)],
             "image_size": (2868, 4310)},
            "DSC_0206":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0207":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0208":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0209":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0210":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0211":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0212":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0213":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0214":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0215":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0216":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0217":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0218":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0219":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0220":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0221":
            {"square_ctr": (2162, 1459),
             "grating_edge": [(1678, 2064), (2351, 2049), (2395, 796), (1678, 810), (1528, 1409),
                              (2273, 2050), (2793, 1985), (2271, 1035), (2483, 795)],
             "white_edge": [(2153, 2372), (3098, 1474), (2131, 481), (1212, 1341), (1229, 2392),
                            (3110, 2357), (3068, 508), (1202, 496)],
             "black_edge": [(2251, 2698), (3403, 1353), (2080, 167), (894, 1371), (3442, 2653),
                            (3373, 167), (882, 179), (939, 2724)],
             "image_size": (2868, 4310)},
            "DSC_0236":
            {"square_ctr": (2446, 1465),
             "grating_edge": [(2596, 2084), (3104, 2064), (3092, 1483), (2748, 784), (2461, 783)],
             "white_edge": [(2395, 2422), (3418, 1558), (2509, 458), (1459, 1391), (1480, 2437)],
             "black_edge": [(2372, 2754), (3750, 1618), (2440, 132), (1118, 416), (1145, 2461)],
             "image_size": (2868, 4310)},
            "DSC_0237":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0238":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0239":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0240":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0241":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0242":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0243":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0244":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0245":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0246":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0247":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0248":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0249":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0250":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0252":
            {"square_ctr": (2467, 1465),
             "grating_edge": [(1914, 2096), (2596, 2081), (2730, 781), (1893, 787), (1812, 1477),
                              (2910, 2075), (2865, 772), (2213, 781), (2225, 2090)],
             "white_edge": [(1690, 2431), (3457, 2330), (3373, 443), (1498, 467), (2437, 2416),
                            (3433, 1447), (2422, 449), (1480, 1501)],
             "black_edge": [(1151, 1361), (2446, 2751), (3765, 1507), (2177, 129), (1202, 2775),
                            (1139, 135), (3702, 111), (3798, 2677)],
             "image_size": (2868, 4310)},
            "DSC_0254":
            {"square_ctr": (2707, 1565),
             "grating_edge": [(2724, 2695), (3904, 2652), (3849, 457), (3345, 283), (2022, 305),
                              (1463, 672), (1485, 2030), (1497, 2690)],
             "white_edge": [(850, 89), (871, 1366), (892, 2753)],
             "black_edge": [(245, 269), (264, 1191), (281, 2597)],
             "image_size": (2868, 4310)},
            "DSC_0255":
            {"square_ctr": (2652, 1434),
             "grating_edge": [(1768, 2707), (2993, 2690), (3823, 2677), (3891, 1645), (3866, 448),
                              (3392, 275), (1607, 309), (1472, 656), (1497, 1958)],
             "white_edge": [(859, 114), (884, 1480), (905, 2593)],
             "black_edge": [(254, 250), (271, 1214), (279, 2398)],
             "image_size": (2868, 4310)},
            "DSC_0256":
            {"square_ctr": (2652, 1434),
             "grating_edge": [(1768, 2707), (2993, 2690), (3823, 2677), (3891, 1645), (3866, 448),
                              (3392, 275), (1607, 309), (1472, 656), (1497, 1958)],
             "white_edge": [(859, 114), (884, 1480), (905, 2593)],
             "black_edge": [(254, 250), (271, 1214), (279, 2398)],
             "image_size": (2868, 4310)},
            "DSC_0257":
            {"square_ctr": (2652, 1434),
             "grating_edge": [(1768, 2707), (2993, 2690), (3823, 2677), (3891, 1645), (3866, 448),
                              (3392, 275), (1607, 309), (1472, 656), (1497, 1958)],
             "white_edge": [(859, 114), (884, 1480), (905, 2593)],
             "black_edge": [(254, 250), (271, 1214), (279, 2398)],
             "image_size": (2868, 4310)},
            "DSC_0259":
            {"interior_edge": [(2237, 1524), (2377, 1486), (2358, 1334), (2198, 1346)],
             "exterior_edge": [(1653, 2634), (3037, 2549), (3616, 1365), (2955, 271), (1516, 314),
                               (925, 1419)],
             "image_size": (2868, 4310)}
            }
