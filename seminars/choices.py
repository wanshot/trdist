# -*- coding: utf-8 -*-
TYPE_CHOICES = (
   (0, '無料'),
   (1, '有料'),
   (2, '展示会'),
)
CATEGORY_CHOICES = (
    ('経営',(
        ('manager01', '経営戦略'),
        ('manager02', '中小企業経営'),
        ('manager03', '起業／開業'),
        ('manager04', 'マネジメント'),
        ('manager05', '業務改善'),
        ('manager06', '経営（その他）'),
        )
    ),
    ('営業',(
        ('sales01', '営業・販売スキル'),
        ('sales02', '顧客満足'),
        ('sales03', 'プレゼンテーション'),
        ('sales04', '営業（その他）'),
        )
    ),
    ('バックオフィス',(
        ('back01', '人材育成・研修'),
        ('back02', '採用'),
        ('back03', '人事／労務'),
        ('back04', '総務／管理'),
        ('back05', '経理／財務'),
        ('back06', 'バックオフィス（その他）'),
        )
    ),
    ('広報・販促',(
        ('pr01', 'マーケティング'),
        ('pr02', 'Webマーケティング'),
        ('pr03', '商品開発'),
        ('pr04', 'プレスリリース'),
        ('pr05', '広報・販促（その他）'),
        )
    ),
    ('ビジネススキル',(
        ('business01', 'ビジネスマナー'),
        ('business02', 'コーチング'),
        ('business03', '自己啓発'),
        ('business04', '接客・接遇'),
        ('business05', 'ビジネススキル（その他）'),
        )
    ),
    ('IT',(
        ('it01', '業務システム'),
        ('it02', 'グループウェア／SFA'),
        ('it03', '情報セキュリティ'),
        ('it04', 'IT（その他）'),
        )
    ),
    ('その他',(
        ('other01', 'その他'),
        )
    ),
)
STATUS_CHOICE = (
    (0, '下書き'),
    (1, '公開'),
    (2, '削除'),
)

