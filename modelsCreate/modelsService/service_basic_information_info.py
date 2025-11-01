"""
业务办理项清单
"""
import uuid
from sqlalchemy import Column, String, CHAR, DateTime, Text, Boolean, func, ForeignKey
from modelsCreate.base import Base


class ServiceBasicInformationInfo(Base):
    __tablename__ = 'service_basic_information_info'

    # 主键：使用 CHAR(36) 存储 UUID 字符串
    rowguid = Column(
        CHAR(36),  # 在数据库中存储为 CHAR(36)
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # 自动生成 UUID 字符串
        nullable=False,
        comment='主键，UUID 自动生成'
    )

    # 外键：关联到 basic_information_info 表的 rowguid
    basic_info_rowguid = Column(
        CHAR(36),
        ForeignKey('basic_information_info.rowguid', ondelete='CASCADE'),
        nullable=False,
        comment='关联 basic_information_info 表的主键'
    )

    # 事项编码
    item_code = Column(String(64), nullable=True, index=True, comment='事项编码')
    # 基本编码
    basic_code = Column(String(64), nullable=True, comment='基本编码')
    # 实施编码
    implement_code = Column(String(64), nullable=True, comment='实施编码')
    # 业务办理项编码
    business_item_code = Column(String(64), nullable=True, comment='业务办理项编码')

    # 办件类型
    handling_type = Column(String(32), nullable=True, comment='办件类型')
    # 事项类型
    item_type = Column(String(32), nullable=True, comment='事项类型')
    # 行使层级
    exercise_level = Column(String(32), nullable=True, comment='行使层级')
    # 法定时限
    legal_limit = Column(String(32), nullable=True, comment='法定时限')
    # 承诺时限
    commitment_limit = Column(String(32), nullable=True, comment='承诺时限')
    # 承诺时限说明
    commitment_limit_explan = Column(Text, nullable=True, comment='承诺时限说明')

    # 实施主体
    implementation_body = Column(String(255), nullable=True, comment='实施主体')
    # 实施主体性质
    body_nature = Column(String(64), nullable=True, comment='实施主体性质')
    # 委托部门
    entrusted_department = Column(String(255), nullable=True, comment='委托部门')
    # 联办机构
    joint_agencies = Column(Text, nullable=True, comment='联办机构')
    # 主办处室
    host_office = Column(String(255), nullable=True, comment='主办处室')

    # 权力来源
    power_source = Column(String(64), nullable=True, comment='权力来源')
    # 联系电话
    contact_phone = Column(String(20), nullable=True, comment='联系电话')
    # 监督投诉电话
    supervision_phone = Column(String(20), nullable=True, comment='监督投诉电话')

    # 特殊环节
    special_links = Column(Text, nullable=True, comment='特殊环节')
    # 一件事集成套餐
    integrated_package = Column(String(255), nullable=True, comment='一件事集成套餐')
    # 市场准入负面清单许可准入措施
    market_access_measures = Column(Text, nullable=True, comment='市场准入负面清单许可准入措施')
    # 中介服务
    intermediary_services = Column(Text, nullable=True, comment='中介服务')
    # 权责清单
    responsibility_list = Column(String(255), nullable=True, comment='权责清单')

    # 审批结果名称
    approval_result_name = Column(String(255), nullable=True, comment='审批结果名称')
    # 审批结果类型
    approval_result_type = Column(String(64), nullable=True, comment='审批结果类型')
    # 审批结果样本
    approval_result_sample = Column(String(255), nullable=True, comment='审批结果样本')
    # 审批结果共享
    approval_result_share = Column(String(32), nullable=True, comment='审批结果共享')
    # 结果领取方式
    result_receive_method = Column(String(64), nullable=True, comment='结果领取方式')
    # 结果领取说明
    result_receive_desc = Column(Text, nullable=True, comment='结果领取说明')

    # 申报对象
    applicant_type = Column(String(64), nullable=True, comment='申报对象')

    # 是否进驻政务大厅
    in_service_hall = Column(Boolean, nullable=True, comment='是否进驻政务大厅')
    # 办理形式
    handling_form = Column(String(64), nullable=True, comment='办理形式')
    # 必须现场办理原因
    must_on_site_reason = Column(Text, nullable=True, comment='必须现场办理原因')

    # 企业办事主题
    person_theme = Column(String(255), nullable=True, comment='个人办事主题')
    # 企业办事主题
    enterprise_theme = Column(String(255), nullable=True, comment='企业办事主题')
    # 网上办理深度
    online_depth = Column(String(32), nullable=True, comment='网上办理深度')

    # 通办范围
    nationwide_coverage = Column(String(64), nullable=True, comment='通办范围')
    # 数量限制
    quantity_limit = Column(String(32), nullable=True, comment='数量限制')
    # 通办范围说明
    coverage_description = Column(Text, nullable=True, comment='通办范围说明')

    # 是否全国高频“跨省通办”事项
    is_national_cross_province = Column(Boolean, nullable=True, comment='是否全国高频“跨省通办”事项')
    # 跨省通办模式
    cross_province_mode = Column(String(64), nullable=True, comment='跨省通办模式')
    # 跨省通办模式说明
    cross_province_explain = Column(Text, nullable=True, comment='跨省通办模式')
    # 跨省代收代办区域
    cross_province_areas = Column(Text, nullable=True, comment='跨省代收代办区域')

    # 计划生效日期
    planned_effective_date = Column(DateTime, nullable=True, comment='计划生效日期')
    # 计划取消日期
    planned_cancel_date = Column(DateTime, nullable=True, comment='计划取消日期')

    # 是否开通预约服务
    has_reservation = Column(Boolean, nullable=True, comment='是否开通预约服务')
    # 是否支持自助终端办理
    support_self_service_terminal = Column(Boolean, nullable=True, comment='是否支持自助终端办理')
    # 面向自然人地方特色主题分类
    individual_theme_category = Column(String(255), nullable=True, comment='面向法人地方特色主题分类')
    # 面向法人地方特色主题分类
    corporate_theme_category = Column(String(255), nullable=True, comment='面向法人地方特色主题分类')

    # 移动端是否对接单点登录
    mobile_sso_enabled = Column(Boolean, nullable=True, comment='移动端是否对接单点登录')
    # 计算机端是否对接单点登录
    pc_sso_enabled = Column(Boolean, nullable=True, comment='计算机端是否对接单点登录')

    # 乡镇街道名称
    town_street_name = Column(String(128), nullable=True, comment='乡镇街道名称')
    # 乡镇街道代码
    town_street_code = Column(String(64), nullable=True, comment='乡镇街道代码')
    # 村镇社区名称
    village_community_name = Column(String(128), nullable=True, comment='村镇社区名称')
    # 村镇社区代码
    village_community_code = Column(String(64), nullable=True, comment='村镇社区代码')

    # 是否支持物流快递
    support_logistics = Column(Boolean, nullable=True, comment='是否支持物流快递')
    # 是否支持网上支付
    support_online_payment = Column(Boolean, nullable=True, comment='是否支持网上支付')

    # 事项状态
    status = Column(String(200), nullable=True, comment='事项状态')
    # 是否全程代办
    full_proxy_enabled = Column(Boolean, nullable=True, comment='是否全程代办')

    # 是否收费
    charge_limit = Column(String(50), nullable=True, comment='是否收费')

    # 备注
    remarks = Column(Text, nullable=True, comment='备注')

    # 项目链接
    dir_link = Column(String(2000), nullable=True, comment='项目链接')

    # 创建时间
    create_date = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')

    def __repr__(self):
        return f"<StandardizedItemCatalog(item_code='{self.item_code}', item_type='{self.item_type}')>"