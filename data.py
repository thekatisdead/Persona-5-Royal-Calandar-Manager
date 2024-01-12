"""
    "person" : {
        "day": 0 for morning, 1 for night
        "schedule": array of days, 0 for sunday 6 for saturday
        "remarks": details you need to know
    }
"""

confidant_list = {
    "yoshida" : {
        "label": "Yoshida (Sun)",
        "day": 1,
        "schedule": [0],
        "remarks": "Yoshida (Sun) needs to be completed before 11/13"
    },
    "makoto" : {
        "label": "Makoto (Priestess)",
        "day": 0,
        "schedule": [0,2,4,6],
        "remarks": "Makoto (Priestess) needs Know 3 for Rank 1 and MAX Charm for Rank 6"
    },
    "haru" : {
        "label": "Haru (Empress)",
        "day": 0,
        "schedule": [1,2,3,4,5,6],
        "remarks": "Haru (Empress) needs MAX Prof for Rank 2"
    },
    "yusuke" : {
        "label": "Yusuke (Emperor)",
        "day": 0,
        "schedule": [0,1,2,3,4,5,6],
        "remarks": "Yusuke (Emperor) needs Prof 4 for Rank 6"
    },
    "sojiro" : {
        "label": "Sojiro (Hierophant)",
        "day": 1,
        "schedule": [0,1,2,4,5,6],
        "remarks": "Sojiro (Hierophant) needs MAX Kind for Rank 7"
    },
    "ann" : {
        "label": "Ann (Lovers)",
        "day": 0,
        "schedule": [0,1,2,3,5],
        "remarks": "Ann (Lovers) needs Kind 2 for Rank 2"
    },
    "ryuji" : {
        "label": "Ryuji (Chariot)",
        "day": 0,
        "schedule": [0,1,2,3,4,5,6],
        "remarks": ""
    },
    "akechi" : {
        "label": "Akechi (Justice)",
        "day": 1,
        "schedule": [3,6],
        "remarks": "Akechi (Justice) needs Know and Charm 3 for Rank 3, Know 4 for Rank 7"
    },
    "futaba" : {
        "label": "Futaba (Hermit)",
        "day": 0,
        "schedule": [0,3,4,6],
        "remarks": "Futaba (Hermit) needs Kind 4 for Rank 2"
    },
    "chiyaya" : {
        "label": "Chihaya (Fortune)",
        "day": 1,
        "schedule": [0,2,4,6],
        "remarks": ""
    },
    "takemi" : {
        "label": "Takemi (Death)",
        "day": 0,
        "schedule": [0,1,2,3,4,5,6],
        "remarks": "Takemi (Death) needs Charm 4 for Rank 2"
    },
    "iwai" : {
        "label": "Iwai (Hanged Man)",
        "day": 1,
        "schedule": [0,4,6],
        "remarks": "Iwai (Hanged Man) needs Guts 4 for Rank 1 and MAX Guts for Rank 8"
    },
    "kawakami" : {
        "label": "Kawakami (Temperance)",
        "day": 1,
        "schedule": [5,6],
        "remarks": ""
    },
    "ohya" : {
        "label": "Ohya (Devil)",
        "day": 1,
        "schedule": [0,1,2,3,4,5,6],
        "remarks": ""
    },
    "oda" : {
        "label": "Oda (Tower)",
        "day": 0,
        "schedule": [1,2,4],
        "remarks": ""
    },
    "hifumi" : {
        "label": "Hifumi (Star)",
        "day": 1,
        "schedule": [0,1,3,6],
        "remarks": "Hifumi (Star) needs Charm 3 for Rank 1 and MAX Know for Rank 8"
    },
    "mishima" : {
        "label": "Mishima (Moon)",
        "day": 1,
        "schedule": [0,1,2,3,4,5,6],
        "remarks": "Mishima (Moon) needs requests completed"
    },
    "maruki" : {
        "label": "Maruki (Councilor)",
        "day": 0,
        "schedule": [1,5],
        "remarks": ""
    },
    "kasumi" : {
        "label": "Kasumi (Faith)",
        "day": 0,
        "schedule": [3,4,6],
        "remarks": "Kasumi (Faith) will be avaiable on Wednesday during 6,9,10,11"
    }
}