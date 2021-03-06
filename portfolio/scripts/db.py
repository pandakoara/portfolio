from flask_script import Command
from portfolio import db 
from datetime import datetime
from portfolio.models.skil import Skil

class InitDB( Command): 
    "create database" 
    
    def run(self):
        db.create_all()

        # 初期データ登録
        db.session.query(Skil).delete()

        skil_data = [
            # s_date, e_date, project, category(1:DB,2:プログラミング言語,3:ツール,4:フレームワーク), os(1:Windows,2:Unix), skil
            ['2004-4', '2005-1', '大手パチンコ企業向けWabサイト運営', 3, 1, 'Excel'],
            ['2004-4', '2005-1', '大手パチンコ企業向けWabサイト運営', 3, 1, 'Word'],
            ['2004-4', '2005-1', '大手パチンコ企業向けWabサイト運営', 3, 1, 'Photoshop'],
            ['2004-4', '2005-1', '大手パチンコ企業向けWabサイト運営', 3, 1, 'FFFTP'],
            ['2005-2', '2005-7', 'コンシューマ・モバイル向けゲーム開発', 3, 1, 'Excel'],
            ['2005-2', '2005-7', 'コンシューマ・モバイル向けゲーム開発', 3, 1, 'Word'],
            ['2005-2', '2005-7', 'コンシューマ・モバイル向けゲーム開発', 3, 1, 'Photoshop'],
            ['2005-2', '2005-7', 'コンシューマ・モバイル向けゲーム開発', 3, 1, 'FFFTP'],
            ['2005-8', '2005-11', '法人企業向け特許管理システム', 2, 1, 'AccessVBA'],
            ['2005-8', '2005-11', '法人企業向け特許管理システム', 1, 1, 'Access'],
            ['2005-12', '2008-10', '証券会社向け株式発注取引管理システム', 2, 2, 'C言語'],
            ['2005-12', '2008-10', '証券会社向け株式発注取引管理システム', 2, 1, 'PL/SQL'],
            ['2005-12', '2008-10', '証券会社向け株式発注取引管理システム', 3, 1, 'JP1'],
            ['2005-12', '2008-10', '証券会社向け株式発注取引管理システム', 1, 1, 'Oracle'],
            ['2008-11', '2009-3', '通信会社向け新設備管理システム', 1, 1, 'Oracle'],
            ['2008-11', '2009-3', '通信会社向け新設備管理システム', 2, 2, 'C言語'],
            ['2008-11', '2009-3', '通信会社向け新設備管理システム', 3, 1, 'JP1'],
            ['2009-4', '2009-8', '携帯キャリア向けゲートウェイシステム', 2, 2, 'C言語'],
            ['2009-4', '2009-8', '携帯キャリア向けゲートウェイシステム', 1, 1, 'Oracle'],
            ['2009-9', '2010-6', '通信会社向けネットワーク監視システム', 1, 1, 'Oracle'],
            ['2009-9', '2010-6', '通信会社向けネットワーク監視システム', 2, 2, 'C言語'],
            ['2009-9', '2010-6', '通信会社向けネットワーク監視システム', 1, 1, 'Wireshark'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 1, 1, 'Oracle'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 1, 2, 'DB2'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 2, 'C言語'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 2, 'Cシェル'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 1, 'Java'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 1, 'JSP'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 3, 1, 'eclipse'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 3, 1, 'JP1'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 1, 'JavaScript'],
            ['2010-7', '2011-10', '銀行向けネットバンキング開発', 2, 1, 'HTML'],
            ['2011-11', '2011-12', '通信会社向けネットワーク監視システム', 2, 2, 'C言語'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 1, 1, 'Oracle'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 1, 2, 'DB2'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 2, 2, 'C言語'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 2, 1, 'Java'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 2, 1, 'JSP'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 3, 1, 'eclipse'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 3, 1, 'JP1'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 2, 1, 'JavaScript'],
            ['2012-1', '2014-9', '銀行向けネットバンキング開発', 2, 1, 'HTML'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 1, 1, 'Oracle'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 3, 1, 'eclipse'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 2, 1, 'Java'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 4, 1, 'intra-mart7.2'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 2, 2, 'C++'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 2, 2, 'Pro*C'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 2, 2, 'Kシェル'],
            ['2014-10', '2017-3', '銀行向け国際系システム開発', 3, 2, 'HULFT'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 1, 1, 'PostgreSQL'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 4, 1, 'Spring-MVC'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 2, 1, 'Java'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 2, 1, 'JSP'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 2, 1, 'jquery'],
            ['2017-4', '2017-9', '一般企業向け素材管理システム開発', 3, 1, 'eclipse'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 1, 1, 'Oracle'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 4, 1, 'TERASOLUNA2'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 4, 1, 'TERASOLUNA5'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 2, 1, 'Java'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 2, 1, 'JSP'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 2, 1, 'javascript'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 2, 1, 'xsl'],
            ['2017-10', '2019-1', '一般社団法人向け電子納税システム開発', 3, 1, 'eclipse'],
            ['2019-2', '-', '不動産管理システム開発', 1, 1, 'Oracle'],
            ['2019-2', '-', '不動産管理システム開発', 4, 1, 'structs'],
            ['2019-2', '-', '不動産管理システム開発', 2, 1, 'Java'],
            ['2019-2', '-', '不動産管理システム開発', 2, 1, 'JSP'],
            ['2019-2', '-', '不動産管理システム開発', 2, 1, 'javascript'],
            ['2019-2', '-', '不動産管理システム開発', 3, 1, 'eclipse'],
            ['2019-2', '-', '不動産管理システム開発', 2, 1, 'ExcelVBA']
            ]

        for sd in skil_data:
            s_date = datetime.strptime(sd[0], '%Y-%m')

            e_date = None
            if sd[1] != '-':
                e_date = datetime.strptime(sd[1], '%Y-%m')

            skil = Skil(s_date = s_date, e_date = e_date, project=sd[2], category=sd[3], os=sd[4], skil=sd[5])
            db.session.add(skil)

        db.session.commit()
