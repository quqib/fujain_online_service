"""
业务办理-基本信息-市场准入负面清单信息表
"""
import uuid
from sqlalchemy import Column, String,CHAR, Text, DateTime, func, ForeignKey
from ..base import Base


class ServiceBasicMarknetAccessInfo(Base):
    __tablename__ = 'service_basic_marknet_access_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 service_basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('service_basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 service_basic_information_info 表的主键'
    )
    # 负面清单表名 进入页面前拿到的那个名称
    market_name = Column(String(200), nullable=True, comment='负面清单表名')

    # ================== 基础信息 ==================
    # 负面清单版本（在用）
    market_negativate_version = Column(String(50), nullable=True, comment='负面清单版本')

    # 负面清单事项状态（在用）
    market_negativate_status = Column(String(50), nullable=True, comment='负面清单事项状态')

    # 负面清单类别（许可准入类）
    market_negativate_type = Column(String(100), nullable=True, comment='负面清单类别')

    # 行业（如“制造业”、“金融业”、“信息技术服务业”）
    market_negativate_industry = Column(String(100), nullable=True, comment='行业')

    # 负面清单事项名称（如“禁止投资烟草制品生产”）
    market_negativate_name = Column(String(500), nullable=True, comment='负面清单事项名称')

    # 负面清单事项编码（国家级统一编码）
    market_negativate_code = Column(String(64), nullable=True, index=True, comment='负面清单事项编码')

    # ================== 措施信息 ==================
    # 负面清单事项措施名称（如“需取得省级主管部门前置审批”）
    market_negativate_measure_name = Column(Text, nullable=True, comment='负面清单事项措施名称')

    # 负面清单事项措施编码
    market_negativate_measure_code = Column(String(64), nullable=True, comment='负面清单事项措施编码')

    # 地方性许可措施（地方自行设定的管理措施）
    local_license_measure = Column(Text, nullable=True, comment='地方性许可措施')

    # 适用范围（如“全国”、“特定区域（自贸区）”）
    applicable_scope = Column(String(2000), nullable=True, comment='适用范围')

    # 事项措施状态（在用）
    market_negativate_measure_status = Column(String(50), nullable=True, comment='事项措施状态')

    # 负面清单事项措施版本
    market_negativate_measure_version = Column(String(50), nullable=True, comment='负面清单事项措施版本')

    # 是否暂时列入清单（如“是”、“否”, -）
    is_temporarily_included = Column(String(2), nullable=True, comment='是否暂时列入清单')  # 可用 '1'=是, '0'=否

    # 计划生效日期
    planned_effective_date = Column(DateTime, nullable=True, comment='计划生效日期')

    # 计划取消日期
    planned_cancel_date = Column(DateTime, nullable=True, comment='计划取消日期')

    # ================== 措施关联匹配 ==================
    # 关联的政务服务事项基本目录（可关联多个，此处存储编码或名称 名称之间使用!@#进行隔开）
    associated_service_item = Column(Text, nullable=True, index=True, comment='政务服务事项基本目录')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<NegativeListInfo(item_code='{self.item_code}', item_name='{self.item_name}', measure_code='{self.measure_code}')>"