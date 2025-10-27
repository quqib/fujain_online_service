from sqlalchemy import Column, String, LargeBinary, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemExtInfo(Base):
    __tablename__ = 'item_ext_info'

    # 主键
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 基础编码信息
    task_code = Column(String(36), nullable=True, comment='实施编码')
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    ywcode_ext = Column(String(100), nullable=True, comment='业务办理项扩展码')
    task_guid = Column(String(50), nullable=True, comment='事项唯一标识')

    # 办理渠道与方式
    service_way = Column(String(2), nullable=True, comment='服务渠道')
    is_online_handle = Column(String(2), nullable=True, comment='是否网办')
    is_schedule = Column(String(2), nullable=True, comment='是否支持预约办理')
    is_pay_online = Column(String(2), nullable=True, comment='是否支持网上支付')
    is_express = Column(String(2), nullable=True, comment='是否支持物流快递')
    is_handle_machine = Column(String(2), nullable=True, comment='是否支持自助终端办理')
    is_voice_handle = Column(String(2), nullable=True, comment='是否视频办')
    is_kdb = Column(String(2), nullable=True, comment='是否可代办')
    is_ydsq = Column(String(2), nullable=True, comment='是否支持异地申请')
    is_ycsl = Column(String(2), nullable=True, comment='是否一窗受理')
    zxsp_type = Column(String(2), nullable=True, comment='网上全程办结')
    online_method = Column(String(100), nullable=True, comment='网办方式')
    online_systype = Column(String(100), nullable=True, comment='网办系统')
    handle_online_address = Column(String(100), nullable=True, comment='网办地址')

    # 进驻与大厅信息
    is_entry_center = Column(String(2), nullable=True, comment='是否进驻政务大厅')
    entrycentertype = Column(String(10), nullable=True, comment='进驻政务大厅类型')
    notentrycenterreason = Column(String(150), nullable=True, comment='未进驻大厅原因')
    jz_hall_name = Column(String(50), nullable=True, comment='大厅名称')
    is_online_qwy = Column(String(2), nullable=True, comment='是否上线秦务员')
    is_sxjj_tysp = Column(String(2), nullable=True, comment='是否上线省级通用审批系统')

    # 通办信息
    handle_area = Column(String(20), nullable=True, comment='通办范围')
    handle_area_explain = Column(String(100), nullable=True, comment='通办范围说明')
    handle_type = Column(String(100), nullable=True, comment='通办类型')
    handle_method = Column(String(100), nullable=True, comment='通办方式')
    yd_handle_area = Column(String(2), nullable=True, comment='异地通办范围')
    transact_addr_map_location = Column(String(100), nullable=True, comment='办理地点点位信息')

    # 材料与受理
    is_sqcl = Column(String(2), nullable=True, comment='是否有申请材料')
    is_need_xcky = Column(String(2), nullable=True, comment='是否需要现场勘验')
    is_need_zztz = Column(String(2), nullable=True, comment='是否需要组织听证')
    is_need_zpgj = Column(String(2), nullable=True, comment='是否需要招标、拍卖、挂牌交易')
    is_need_check = Column(String(2), nullable=True, comment='是否需要检验、检测、检疫')
    is_need_jd = Column(String(2), nullable=True, comment='是否需要鉴定')
    is_need_zjps = Column(String(2), nullable=True, comment='是否需要专家评审')
    is_need_openshow = Column(String(2), nullable=True, comment='是否需要向社会公示')

    # 审批结果
    result_type = Column(String(30), nullable=True, comment='审批结果类型')
    result_name = Column(String(200), nullable=True, comment='审批结果名称')
    result_guid = Column(String(100), nullable=True, comment='审批结果样本')
    result_dec = Column(String(30), nullable=True, comment='审批结果形式')
    express_content = Column(String(100), nullable=True, comment='审批结果通知方式和送达方式')
    express_send_type = Column(String(100), nullable=True, comment='物流快递内容')
    result_send_mode = Column(String(100), nullable=True, comment='审批结果送达方式')
    is_result_cert = Column(String(2), nullable=True, comment='是否电子证照')
    result_cert_name = Column(String(100), nullable=True, comment='电子证照名称')
    result_cert_code = Column(String(50), nullable=True, comment='电子证照编码')

    # 行政许可专项字段
    xzxk_item_type = Column(String(2), nullable=True, comment='行政许可事项类型')
    zyxk_condition = Column(String(100), nullable=True, comment='准予行政许可的条件')
    gdxk_condition_law = Column(String(100), nullable=True, comment='规定行政许可条件的依据')
    gdxk_process_law = Column(String(200), nullable=True, comment='规定行政许可程序的依据')
    xkzj_name = Column(String(200), nullable=True, comment='行政许可证件名称')
    xkzj_limit_time = Column(String(200), nullable=True, comment='行政许可证件的有效期限')
    xkzj_limit_type = Column(String(50), nullable=True, comment='行政许可证件的有效期限单位')
    xkzj_limit_law = Column(String(200), nullable=True, comment='规定行政许可证件有效期限的依据')
    xkzj_limit_yq = Column(String(200), nullable=True, comment='办理行政许可证件延续手续的要求')
    xkzj_limit_area = Column(String(200), nullable=True, comment='行政许可证件的有效地域范围')
    xkzj_limit_otherarea = Column(String(200), nullable=True, comment='行政许可证件的有效地域范围其他说明')
    xkzj_limit_arealaw = Column(String(200), nullable=True, comment='规定行政许可证件有效地域范围的依据')

    # 数量限制
    is_limit_explain = Column(String(2), nullable=True, comment='有无行政许可数量限制')
    limit_explain = Column(LargeBinary, nullable=True, comment='数量限制')
    limit_explain_yj = Column(String(100), nullable=True, comment='数量限制依据')
    open_limit_fs = Column(String(200), nullable=True, comment='公布数量限制的方式')
    open_limit_fsother = Column(String(200), nullable=True, comment='公布数量限制的其他方式说明')
    open_limit_time = Column(String(200), nullable=True, comment='公布数量限制的周期')
    open_limit_type = Column(String(50), nullable=True, comment='公布数量限制的周期单位')
    xzxk_limit_mode = Column(String(50), nullable=True, comment='在数量限制条件下实施行政许可的方式')
    xzxk_limit_mother = Column(String(200), nullable=True, comment='在数量限制条件下实施行政许可的其他方式说明')
    by_law_xzxk = Column(String(200), nullable=True, comment='规定在数量限制条件下实施行政许可方式的依据')

    # 年检与年报
    is_njyq = Column(String(2), nullable=True, comment='有无年检要求')
    by_law_nj = Column(String(200), nullable=True, comment='设定年检要求的依据')
    njzq = Column(String(2), nullable=True, comment='年检周期')
    njzq_dec = Column(String(200), nullable=True, comment='年检周期其他说明')
    is_nj_material = Column(String(2), nullable=True, comment='年检是否需要报送材料')
    is_njfee = Column(String(2), nullable=True, comment='年检是否收费')
    is_xzfy = Column(String(2), nullable=True, comment='有无年报要求')
    nbzq = Column(String(2), nullable=True, comment='年报周期')
    nbzq_dec = Column(String(200), nullable=True, comment='年报周期其他说明')
    material_name_nb = Column(String(200), nullable=True, comment='年报报送材料名称')

    # 中介服务
    is_service_dept = Column(String(2), nullable=True, comment='有无中介服务事项')
    service_dept_name = Column(String(200), nullable=True, comment='中介服务事项名称')
    service_dept_law = Column(String(200), nullable=True, comment='设定中介服务事项的依据')
    service_dept_jg = Column(String(200), nullable=True, comment='提供中介服务事项的机构')
    service_dept_feetype = Column(String(10), nullable=True, comment='中介服务事项收费性质')
    service_dept = Column(String(100), nullable=True, comment='中介服务')
    service_dept_extend = Column(String(200), nullable=True, comment='中介服务清单')

    # 联办与共同办理
    other_dept = Column(String(100), nullable=True, comment='联办机构')
    other_dept_s = Column(String(100), nullable=True, comment='联办机构适用情形')
    other_togetoffice = Column(String(100), nullable=True, comment='其他共同办理处室')

    # 主题分类
    theme_natural_type = Column(String(100), nullable=True, comment='面向自然人事项主题分类')
    theme_legal_type = Column(String(100), nullable=True, comment='面向法人事项主题分类')
    theme_natural_type_ts = Column(String(100), nullable=True, comment='面向自然人地方特色主题分类')
    theme_legal_type_ts = Column(String(100), nullable=True, comment='面向法人地方特色主题分类')

    # 办理依据与标准
    handle_yj = Column(LargeBinary, nullable=True, comment='办理依据')
    rul_stand = Column(LargeBinary, nullable=True, comment='裁决标准')
    prohibit_law = Column(String(200), nullable=True, comment='禁止性规定')
    xz_procedure = Column(String(200), nullable=True, comment='行政程序')

    # 承诺制与告知承诺
    is_inform_promise = Column(String(2), nullable=True, comment='是否实行告知承诺办理')
    inform_promise_explain = Column(String(200), nullable=True, comment='告知承诺说明')
    inform_promise_file = Column(String(100), nullable=True, comment='告知承诺书')
    eformName = Column(String(200), nullable=True, comment='关联电子表单名称')
    eformId = Column(String(50), nullable=True, comment='关联电子表单Id')

    # 收件信息
    recp_name = Column(String(100), nullable=True, comment='收件人姓名')
    recp_phone = Column(String(100), nullable=True, comment='收件人电话')
    recp_address = Column(String(200), nullable=True, comment='收件人地址')
    zip_code = Column(String(100), nullable=True, comment='邮政编码')
    zip_explain = Column(String(100), nullable=True, comment='邮寄说明')
    express_fee = Column(String(200), nullable=True, comment='快递费用')
    express_fee_object = Column(String(5), nullable=True, comment='快递费用说明')

    # 法律救济渠道
    slxzfy_office = Column(String(100), nullable=True, comment='是否行政复议')
    slxzfy_office_tel = Column(String(100), nullable=True, comment='受理行政复议部门')
    slxzfy_office_add = Column(String(100), nullable=True, comment='受理行政复议部门电话')
    reconsideration_channel = Column(String(450), nullable=True, comment='行政复议途径')
    slxzss_office = Column(String(100), nullable=True, comment='是否行政诉讼')
    slxzss_office_tel = Column(String(100), nullable=True, comment='受理行政诉讼部门')
    slxzss_office_add = Column(String(100), nullable=True, comment='受理行政诉讼部门电话')
    lawsuits_channel = Column(String(550), nullable=True, comment='行政诉讼途径')

    # 特殊事项标识
    is_quiet_item = Column(String(2), nullable=True, comment='是否为静默事项')
    is_zmq_item = Column(String(2), nullable=True, comment='是否自贸区事项')
    fta_cancel_explain = Column(String(200), nullable=True, comment='自贸区取消说明')
    isindustrialland_reform = Column(String(2), nullable=True, comment='是否属于“工改”事项')
    suitable_for_old = Column(String(2), nullable=True, comment='是否属于“适老化”事项')
    record_system_explain = Column(String(200), nullable=True, comment='备案制度说明')

    # 系统对接与建设
    system_type = Column(String(100), nullable=True, comment='系统所属类型')
    system_name = Column(String(100), nullable=True, comment='系统名称')
    system_net = Column(String(100), nullable=True, comment='系统网络运行环境')
    syslink_method = Column(String(100), nullable=True, comment='系统联系方式')
    author_level = Column(String(100), nullable=True, comment='认证等级')
    sjblsd = Column(String(100), nullable=True, comment='事项办理深度')
    wsblsd = Column(String(20), nullable=True, comment='网上办理深度')
    is_show_guide = Column(String(2), nullable=True, comment='是否展示办事指南')
    is_online = Column(String(2), nullable=True, comment='是否上线')
    linkwith_p_hall = Column(String(2), nullable=True, comment='与省级大厅完成对接')
    use_ty_platform = Column(String(2), nullable=True, comment='使用统一受理平台')
    dj_type = Column(String(2), nullable=True, comment='数据对接类型')
    id_test_type = Column(String(2), nullable=True, comment='接入统一办件库')
    online_qc_bj = Column(String(2), nullable=True, comment='网上全程办结')
    yeblxtname = Column(String(200), nullable=True, comment='业务办理系统名称')

    # 地域信息（乡镇街道）
    xzjdmc = Column(String(200), nullable=True, comment='乡镇街道名称')
    xzjddm = Column(String(50), nullable=True, comment='乡镇街道代码')
    cjsqmc = Column(String(200), nullable=True, comment='村居社区名称')
    cjsqdm = Column(String(50), nullable=True, comment='村居社区代码')

    # 其他
    is_legal_auth = Column(String(2), nullable=True, comment='是否法人授权事项')
    is_confident = Column(String(2), nullable=True, comment='是否涉密')
    remark = Column(String(100), nullable=True, comment='备注说明')
    tzcorp_address = Column(String(100), nullable=True, comment='企业投资项目申报地址')
    entrust_file = Column(String(100), nullable=True, comment='委托书')
    id_test_type = Column(String(2), nullable=True, comment='身份验证类型')
    query_method = Column(String(2000), nullable=True, comment='办理进程及结果查询途径')
    create_date = Column(Date, nullable=True, comment='创建日期')
    update_date = Column(Date, nullable=True, comment='更新日期')
    state = Column(String(1), nullable=True, comment='状态')

    def __repr__(self):
        return f"<ItemExtInfo(task_code={self.task_code}, ywcode={self.ywcode})>"