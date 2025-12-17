# 詳細差分（モジュール別）

## モジュール追加/削除まとめ
- 追加されたモジュール:
  - quel_ic_config.ad9082: [quel_ic_config/src/quel_ic_config/ad9082.py](quel_ic_config/src/quel_ic_config/ad9082.py)
  - quel_ic_config.box_force_unlock: [quel_ic_config/src/quel_ic_config/box_force_unlock.py](quel_ic_config/src/quel_ic_config/box_force_unlock.py)
  - quel_ic_config.box_lock: [quel_ic_config/src/quel_ic_config/box_lock.py](quel_ic_config/src/quel_ic_config/box_lock.py)
  - quel_ic_config.exstickge_sock_client: [quel_ic_config/src/quel_ic_config/exstickge_sock_client.py](quel_ic_config/src/quel_ic_config/exstickge_sock_client.py)
  - quel_ic_config.quel1_thermistor: [quel_ic_config/src/quel_ic_config/quel1_thermistor.py](quel_ic_config/src/quel_ic_config/quel1_thermistor.py)
  - quel_ic_config.quel1se_config_subsystem: [quel_ic_config/src/quel_ic_config/quel1se_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1se_config_subsystem.py)
  - quel_ic_config.quel_clock_master_v1: [quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py](quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py)
- 削除されたモジュール:
  - quel_ic_config.ad9082_v106: [v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py](v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py)
  - quel_ic_config.e7workaround: [v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py](v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py)
  - quel_ic_config.generic_gpio: [v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py](v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py)
  - quel_ic_config.quel1_box_with_raw_wss: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py)
  - quel_ic_config.thermistor: [v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py](v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py)

## quel_ic_config.ad9082
- 新: [quel_ic_config/src/quel_ic_config/ad9082.py](quel_ic_config/src/quel_ic_config/ad9082.py)
- 追加された関数: update_mapping_recursive
- 追加されたクラス: Ad9082AdcConfig, Ad9082ChannelAssignConfig, Ad9082ClockConfig, Ad9082ComplexToRealEnableConfig, Ad9082Config, Ad9082DacConfig, Ad9082DecimationRateConfig, Ad9082DesConfig, Ad9082InterpolationRateConfig, Ad9082JesdParam, Ad9082Mixin, Ad9082SerConfig, Ad9082SerdesConfig, Ad9082ShiftFreqConfig, Ad9082SpiAddrNextConfigEnum, Ad9082SpiConfig, Ad9082SpiMsbConfigEnum, Ad9082SpiPinConfigEnum, FrozenRootModel, FrozenSequenceRootModel, NcoFtw, NoExtraBaseModel
- クラス `Ad9082ChannelAssignConfig` のメソッド差分:
  - 追加: as_cpptype, dac0_order, dac1_order, dac2_order, dac3_order, dac_order
- クラス `Ad9082JesdParam` のメソッド差分:
  - 追加: as_cpptype
- クラス `Ad9082Mixin` のメソッド差分:
  - 追加: calc_adc_cnco_freq, calc_adc_cnco_ftw, calc_adc_fnco_freq, calc_adc_fnco_ftw, calc_dac_cnco_freq, calc_dac_cnco_ftw, calc_dac_fnco_freq, calc_dac_fnco_ftw, clear_crc_error, configure, decode_fullscale_current, device_chip_id_get, device_clk_config_set, device_init, device_reset, dump_jesd_status, dump_regs, get_adc_clk_div, get_adc_cnco, get_adc_decimation_rates, get_adc_fnco, get_channel_decimation_rate, get_channel_interpolation_rate, get_crc_error_counts, get_dac_cnco, get_dac_fnco, get_dac_interpolation_rates, get_fduc_of_dac, get_fullscale_current, get_link_status, get_main_decimation_rate, get_main_interpolation_rate, get_pll_bypassed, get_temperatures, get_virtual_adc_select, hal_reg_get, hal_reg_set, is_bgcal_enabled, is_equal_fullscale_current, is_equivalent_adc_cnco, is_equivalent_adc_fnco, is_equivalent_dac_cnco, is_equivalent_dac_fnco, read_reg, reconnect, set_adc_cnco, set_adc_fnco, set_dac_cnco, set_dac_fnco, set_fullscale_current, write_reg
- クラス `Ad9082SpiAddrNextConfigEnum` のメソッド差分:
  - 追加: as_cpptype
- クラス `Ad9082SpiMsbConfigEnum` のメソッド差分:
  - 追加: as_cpptype
- クラス `Ad9082SpiPinConfigEnum` のメソッド差分:
  - 追加: as_cpptype
- クラス `NcoFtw` のメソッド差分:
  - 追加: from_ftw, to_ftw

## quel_ic_config.ad9082_v106
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py](v0.8.11/quel_ic_config/src/quel_ic_config/ad9082_v106.py)
- 削除された関数: update_mapping_recursive
- 削除されたクラス: Ad9082AdcConfig, Ad9082ChannelAssignConfig, Ad9082ClockConfig, Ad9082ComplexToRealEnableConfig, Ad9082Config, Ad9082DacConfig, Ad9082DecimationRateConfig, Ad9082DesConfig, Ad9082InterpolationRateConfig, Ad9082JesdParam, Ad9082SerConfig, Ad9082SerdesConfig, Ad9082ShiftFreqConfig, Ad9082SpiAddrNextConfigEnum, Ad9082SpiConfig, Ad9082SpiMsbConfigEnum, Ad9082SpiPinConfigEnum, Ad9082V106Mixin, FrozenRootModel, FrozenSequenceRootModel, NcoFtw, NoExtraBaseModel
- クラス `Ad9082ChannelAssignConfig` のメソッド差分:
  - 削除: as_cpptype, dac0_order, dac1_order, dac2_order, dac3_order, dac_order
- クラス `Ad9082JesdParam` のメソッド差分:
  - 削除: as_cpptype
- クラス `Ad9082SpiAddrNextConfigEnum` のメソッド差分:
  - 削除: as_cpptype
- クラス `Ad9082SpiMsbConfigEnum` のメソッド差分:
  - 削除: as_cpptype
- クラス `Ad9082SpiPinConfigEnum` のメソッド差分:
  - 削除: as_cpptype
- クラス `Ad9082V106Mixin` のメソッド差分:
  - 削除: calc_adc_cnco_freq, calc_adc_cnco_ftw, calc_adc_fnco_freq, calc_adc_fnco_ftw, calc_dac_cnco_freq, calc_dac_cnco_ftw, calc_dac_fnco_freq, calc_dac_fnco_ftw, clear_crc_error, configure, decode_fullscale_current, device_chip_id_get, device_clk_config_set, device_init, device_reset, dump_jesd_status, dump_regs, get_adc_clk_div, get_adc_cnco, get_adc_decimation_rates, get_adc_fnco, get_channel_decimation_rate, get_channel_interpolation_rate, get_crc_error_counts, get_dac_cnco, get_dac_fnco, get_dac_interpolation_rates, get_fduc_of_dac, get_fullscale_current, get_link_status, get_main_decimation_rate, get_main_interpolation_rate, get_pll_bypassed, get_temperatures, get_virtual_adc_select, hal_reg_get, hal_reg_set, is_bgcal_enabled, is_equal_fullscale_current, is_equivalent_adc_cnco, is_equivalent_adc_fnco, is_equivalent_dac_cnco, is_equivalent_dac_fnco, read_reg, reconnect, set_adc_cnco, set_adc_fnco, set_dac_cnco, set_dac_fnco, set_fullscale_current, write_reg
- クラス `NcoFtw` のメソッド差分:
  - 削除: from_ftw, to_ftw

## quel_ic_config.box_force_unlock
- 新: [quel_ic_config/src/quel_ic_config/box_force_unlock.py](quel_ic_config/src/quel_ic_config/box_force_unlock.py)
- 追加された関数: force_unlock_all_boxes

## quel_ic_config.box_lock
- 新: [quel_ic_config/src/quel_ic_config/box_lock.py](quel_ic_config/src/quel_ic_config/box_lock.py)
- 追加された関数: guarded_by_box_lock, set_trancated_traceback_for_lock_error
- 追加されたクラス: BoxLockError

## quel_ic_config.e7resource_mapper
- 新: [quel_ic_config/src/quel_ic_config/e7resource_mapper.py](quel_ic_config/src/quel_ic_config/e7resource_mapper.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/e7resource_mapper.py](v0.8.11/quel_ic_config/src/quel_ic_config/e7resource_mapper.py)
- 追加された関数: create_rmap_object, validate_configuration_integrity
- 追加されたクラス: AbstractQuel1E7ResourceMapper, Quel1ConventionalE7ResourceMapper
- 削除されたクラス: Quel1E7ResourceMapper
- クラス `AbstractQuel1E7ResourceMapper` のメソッド差分:
  - 追加: get_awg_from_fduc, get_awgs_of_mxfe, get_capmod_from_fddc, get_fduc_from_awg
- クラス `Quel1E7ResourceMapper` のメソッド差分:
  - 削除: get_active_adc, get_active_adc_of_mxfe, get_active_rlines_of_group, get_active_rlines_of_mxfe, get_awg_of_channel, get_awg_of_line, get_awgs_of_mxfe, get_capture_module_of_adc, get_capture_module_of_rline, get_capture_units_of_rline, get_rchannel_of_runit, get_rchannels_of_rline, resolve_rline, validate_configuration_integrity

## quel_ic_config.e7workaround
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py](v0.8.11/quel_ic_config/src/quel_ic_config/e7workaround.py)
- 削除された関数: detect_branch_of_library, resolve_hw_type
- 削除されたクラス: CaptureModule, CaptureUnit, E7FwLifeStage, E7FwType, E7LibBranch
- クラス `CaptureModule` のメソッド差分:
  - 削除: all, get_units, includes, of
- クラス `CaptureUnit` のメソッド差分:
  - 削除: all, includes, of

## quel_ic_config.exstickge_coap_client
- 新: [quel_ic_config/src/quel_ic_config/exstickge_coap_client.py](quel_ic_config/src/quel_ic_config/exstickge_coap_client.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/exstickge_coap_client.py](v0.8.11/quel_ic_config/src/quel_ic_config/exstickge_coap_client.py)
- 追加されたクラス: AbstractSyncAsyncCoapClient, SyncAsyncCoapClientWithDeviceLock, SyncAsyncCoapClientWithDummyLock, SyncAsyncCoapClientWithFileLock
- 削除されたクラス: SyncAsyncCoapClient
- クラス `AbstractSyncAsyncCoapClient` のメソッド差分:
  - 追加: has_lock, release_lock_all, release_lock_all_at_exit, request, request_and_wait, run, terminate
- クラス `SyncAsyncCoapClient` のメソッド差分:
  - 削除: request, request_and_wait, run, terminate
- クラス `SyncAsyncCoapClientWithDeviceLock` のメソッド差分:
  - 追加: terminate
- クラス `SyncAsyncCoapClientWithDummyLock` のメソッド差分:
  - 追加: terminate

## quel_ic_config.exstickge_sock_client
- 新: [quel_ic_config/src/quel_ic_config/exstickge_sock_client.py](quel_ic_config/src/quel_ic_config/exstickge_sock_client.py)
- 追加されたクラス: AbstractLockKeeper, DummyLockKeeper, FileLockKeeper
- クラス `AbstractLockKeeper` のメソッド差分:
  - 追加: activate, deactivate, has_lock, release_lock_all, run
- クラス `DummyLockKeeper` のメソッド差分:
  - 追加: has_lock
- クラス `FileLockKeeper` のメソッド差分:
  - 追加: has_lock

## quel_ic_config.generic_gpio
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py](v0.8.11/quel_ic_config/src/quel_ic_config/generic_gpio.py)
- 削除されたクラス: GenericGpioConfigHelper, GenericGpioMixin, Gpio14
- クラス `GenericGpioConfigHelper` のメソッド差分:
  - 削除: flush
- クラス `GenericGpioMixin` のメソッド差分:
  - 削除: dump_regs
- クラス `Gpio14` のメソッド差分:
  - 削除: build, parse

## quel_ic_config.linkupper
- 新: [quel_ic_config/src/quel_ic_config/linkupper.py](quel_ic_config/src/quel_ic_config/linkupper.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/linkupper.py](v0.8.11/quel_ic_config/src/quel_ic_config/linkupper.py)
- クラス `LinkupFpgaMxfe` のメソッド差分:
  - 追加: check_all_fddcs_of_mxfe_at_reconnect, check_all_fddcs_of_mxfe_at_relinkup, check_fddc
  - 削除: check_adc, check_all_adcs_of_mxfe_at_reconnect, check_all_adcs_of_mxfe_at_relinkup

## quel_ic_config.quel1_any_config_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1_any_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1_any_config_subsystem.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_any_config_subsystem.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_any_config_subsystem.py)
- 追加されたクラス: Quel1seAnyConfigSubsystem
- クラス `Quel1AnyConfigSubsystem` のメソッド差分:
  - 追加: get_fddc_idx, get_mxfe_temperature_range, has_lock, initialize
  - 変更: get_fduc_idx(旧: (self, group, line)) → (新: (self, group, line, channel))
- クラス `Quel1seAnyConfigSubsystem` のメソッド差分:
  - 追加: get_actuator_desc, get_tempctrl_actuator_output, get_tempctrl_setpoint, get_tempctrl_temperature, get_thermistor_desc, set_tempctrl_setpoint

## quel_ic_config.quel1_box
- 新: [quel_ic_config/src/quel_ic_config/quel1_box.py](quel_ic_config/src/quel_ic_config/quel1_box.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box.py)
- 追加された関数: parse_port_str
- 追加されたクラス: BoxStartCapunitsByTriggerTask, BoxStartCapunitsNowTask
- クラス `Quel1Box` のメソッド差分:
  - 追加: delete_wavedata, get_averaged_sysref_offset, get_current_timecounter, get_latest_sysref_timecounter, get_names_of_wavedata, get_ports_sharing_physical_port, has_lock, has_wavedata, initialize, initialize_all_awgunits, is_valid_port, name, register_wavedata, start_capture_by_awg_trigger, start_capture_now, start_wavegen
  - 削除: capture_start, easy_capture, easy_start_cw, easy_stop, easy_stop_all, initialize_all_awgs, load_cw_into_channel, load_iq_into_channel, prepare_for_emission, read_current_and_latched_clock, read_current_clock, reserve_emission, simple_capture_start, sss, start_emission, stop_emission
  - 変更: config_channel(旧: (self, port, channel, subport, fnco_freq)) → (新: (self, port, channel, fnco_freq, awg_param))
  - 変更: config_port(旧: (self, port, subport, lo_freq, cnco_freq, cnco_locked_with, vatt, sideband, fullscale_current, rfswitch)) → (新: (self, port, lo_freq, cnco_freq, cnco_locked_with, vatt, sideband, fullscale_current, rfswitch))
  - 変更: config_runit(旧: (self, port, runit, fnco_freq)) → (新: (self, port, runit, fnco_freq, capture_param))
  - 変更: create(旧: (cls, ipaddr_wss, ipaddr_sss, ipaddr_css, boxtype, skip_init, **options)) → (新: (cls, ipaddr_wss, ipaddr_sss, ipaddr_css, boxtype, skip_init, name, **options))
  - 変更: dump_port(旧: (self, port, subport)) → (新: (self, port))
  - 変更: dump_rfswitch(旧: (self, port, subport)) → (新: (self, port))
  - 変更: get_loopbacks_of_port(旧: (self, port, subport)) → (新: (self, port))
  - 変更: is_input_port(旧: (self, port_subport)) → (新: (self, port))
  - 変更: is_monitor_input_port(旧: (self, port_subport)) → (新: (self, port))
  - 変更: is_output_port(旧: (self, port_subport)) → (新: (self, port))
  - 変更: is_read_input_port(旧: (self, port_subport)) → (新: (self, port))
  - 変更: relinkup(旧: (self, param, config_root, config_options, mxfes_to_linkup, hard_reset, use_204b, use_bg_cal, skip_init, background_noise_threshold, ignore_crc_error_of_mxfe, ignore_access_failure_of_adrf6780, ignore_lock_failure_of_lmx2594, ignore_extraordinary_converter_select_of_mxfe, restart_tempctrl)) → (新: (self, param, config_root, config_options, mxfes_to_linkup, hard_reset, use_204b, use_bg_cal, skip_init, hard_reset_wss, background_noise_threshold, ignore_crc_error_of_mxfe, ignore_access_failure_of_adrf6780, ignore_lock_failure_of_lmx2594, ignore_extraordinary_converter_select_of_mxfe, restart_tempctrl))

## quel_ic_config.quel1_box_intrinsic
- 新: [quel_ic_config/src/quel_ic_config/quel1_box_intrinsic.py](quel_ic_config/src/quel_ic_config/quel1_box_intrinsic.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_intrinsic.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_intrinsic.py)
- 追加された関数: create_css_wss_rmap
- 追加されたクラス: BoxIntrinsicStartCapunitsByTriggerTask, BoxIntrinsicStartCapunitsNowTask
- クラス `Quel1BoxIntrinsic` のメソッド差分:
  - 追加: delete_wavedata, get_averaged_sysref_offset, get_current_timecounter, get_latest_sysref_timecounter, get_names_of_wavedata, hardreset_wss_units, has_lock, has_wavedata, initialize_all_awgunits, register_wavedata, start_capture_by_awg_trigger, start_capture_now, start_wavegen
  - 削除: capture_start, easy_capture, easy_start_cw, easy_stop, easy_stop_all, initialize_all_awgs, load_cw_into_channel, load_iq_into_channel, prepare_for_emission, read_current_and_latched_clock, read_current_clock, reserve_emission, simple_capture_start, sss, start_emission, stop_emission
  - 変更: config_channel(旧: (self, group, line, channel, fnco_freq)) → (新: (self, group, line, channel, fnco_freq, awg_param))
  - 変更: config_runit(旧: (self, group, rline, runit, fnco_freq)) → (新: (self, group, rline, runit, fnco_freq, capture_param))
  - 変更: relinkup(旧: (self, param, config_root, config_options, mxfes_to_linkup, hard_reset, use_204b, use_bg_cal, skip_init, background_noise_threshold, ignore_crc_error_of_mxfe, ignore_access_failure_of_adrf6780, ignore_lock_failure_of_lmx2594, ignore_extraordinary_converter_select_of_mxfe, restart_tempctrl)) → (新: (self, param, config_root, config_options, mxfes_to_linkup, hard_reset, use_204b, use_bg_cal, skip_init, hard_reset_wss, background_noise_threshold, ignore_crc_error_of_mxfe, ignore_access_failure_of_adrf6780, ignore_lock_failure_of_lmx2594, ignore_extraordinary_converter_select_of_mxfe, restart_tempctrl))

## quel_ic_config.quel1_box_with_raw_wss
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_box_with_raw_wss.py)
- 削除されたクラス: Quel1BoxWithRawWss
- クラス `Quel1BoxWithRawWss` のメソッド差分:
  - 削除: config_channel, config_runit, create

## quel_ic_config.quel1_config_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1_config_subsystem.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem.py)
- 追加されたクラス: AbstractExstickgeSockClientQuel1, Ad9082Quel1, ExstickgeSockClientQuel1WithDummyLock, ExstickgeSockClientQuel1WithFileLock, Quel1ConfigSubsystemAd9082Mixin
- 削除されたクラス: ExstickgeSockClientQuel1
- クラス `Quel1ConfigSubsystem` のメソッド差分:
  - 追加: initialize
- クラス `QuelMeeBoardConfigSubsystem` のメソッド差分:
  - 追加: initialize

## quel_ic_config.quel1_config_subsystem_common
- 新: [quel_ic_config/src/quel_ic_config/quel1_config_subsystem_common.py](quel_ic_config/src/quel_ic_config/quel1_config_subsystem_common.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem_common.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem_common.py)
- 追加されたクラス: Quel1GenericConfigSubsystemAd9082Mixin
- 削除されたクラス: Quel1ConfigSubsystemAd9082Mixin, Quel1ConfigSubsystemGpioMixin
- クラス `Quel1ConfigSubsystemAd9082Mixin` のメソッド差分:
  - 削除: ad9082, allow_dual_modulus_nco, check_link_status, clear_crc_error, get_ad9082_temperatures, get_adc_cnco, get_adc_fnco, get_adc_idx, get_channel_interpolation_rate, get_crc_error_counts, get_dac_cnco, get_dac_fnco, get_dac_idx, get_fduc_idx, get_fullscale_current, get_link_status, get_main_interpolation_rate, get_num_channels_of_line, get_num_rchannels_of_rline, get_rline_from_adc_idx, get_virtual_adc_select, is_equal_fullscale_current, is_equivalent_adc_cnco, is_equivalent_adc_fnco, is_equivalent_dac_cnco, is_equivalent_dac_fnco, set_adc_cnco, set_adc_fnco, set_dac_cnco, set_dac_fnco, set_fullscale_current, set_pair_cnco, validate_chip_id
- クラス `Quel1ConfigSubsystemBaseSlot` のメソッド差分:
  - 追加: has_lock
- クラス `Quel1ConfigSubsystemGpioMixin` のメソッド差分:
  - 削除: gpio, gpio_helper, init_gpio
- クラス `Quel1ConfigSubsystemRoot` のメソッド差分:
  - 追加: initialize
- クラス `Quel1GenericConfigSubsystemAd9082Mixin` のメソッド差分:
  - 追加: ad9082, allow_dual_modulus_nco, check_link_status, clear_crc_error, get_adc_cnco, get_adc_fnco, get_adc_idx, get_channel_interpolation_rate, get_crc_error_counts, get_dac_cnco, get_dac_fnco, get_dac_idx, get_fddc_idx, get_fduc_idx, get_fullscale_current, get_link_status, get_main_interpolation_rate, get_mxfe_temperature_range, get_num_channels_of_line, get_num_rchannels_of_rline, get_rline_from_adc_idx, get_virtual_adc_select, is_equal_fullscale_current, is_equivalent_adc_cnco, is_equivalent_adc_fnco, is_equivalent_dac_cnco, is_equivalent_dac_fnco, set_adc_cnco, set_adc_fnco, set_dac_cnco, set_dac_fnco, set_fullscale_current, set_pair_cnco, validate_chip_id

## quel_ic_config.quel1_config_subsystem_tempctrl
- 新: [quel_ic_config/src/quel_ic_config/quel1_config_subsystem_tempctrl.py](quel_ic_config/src/quel_ic_config/quel1_config_subsystem_tempctrl.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem_tempctrl.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_config_subsystem_tempctrl.py)
- クラス `Quel1seConfigSubsystemTempctrlMixin` のメソッド差分:
  - 追加: get_actuator_desc, get_thermistor_desc

## quel_ic_config.quel1_thermistor
- 新: [quel_ic_config/src/quel_ic_config/quel1_thermistor.py](quel_ic_config/src/quel_ic_config/quel1_thermistor.py)
- 追加されたクラス: Quel1NormalThermistor, Quel1PathSelectorThermistor, Quel1Thermistor, Quel1seExternalThermistor, Quel1seOnboardThermistor
- クラス `Quel1NormalThermistor` のメソッド差分:
  - 追加: convert
- クラス `Quel1PathSelectorThermistor` のメソッド差分:
  - 追加: convert
- クラス `Quel1Thermistor` のメソッド差分:
  - 追加: convert
- クラス `Quel1seExternalThermistor` のメソッド差分:
  - 追加: convert
- クラス `Quel1seOnboardThermistor` のメソッド差分:
  - 追加: convert

## quel_ic_config.quel1_wave_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1_wave_subsystem.py](quel_ic_config/src/quel_ic_config/quel1_wave_subsystem.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1_wave_subsystem.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1_wave_subsystem.py)
- 追加されたクラス: AbstractCancellableTask, AbstractCancellableTaskWrapper, AbstractStartAwgunitsTask, AbstractStartCapunitsTask, StartAwgunitsNowTask, StartAwgunitsTimedTask, StartCapunitsByTriggerTask, StartCapunitsNowTask
- 削除されたクラス: CaptureResults
- クラス `AbstractCancellableTask` のメソッド差分:
  - 追加: cancel, cancelled, done, exception, is_started, result, running, start
- クラス `AbstractCancellableTaskWrapper` のメソッド差分:
  - 追加: cancel, cancelled, done, exception, is_started, result, running, start
- クラス `AbstractStartAwgunitsTask` のメソッド差分:
  - 追加: has_started_emission, wait_for_starting_emission
- クラス `Quel1WaveSubsystem` のメソッド差分:
  - 追加: config_awgunit, config_capunit, delete_wavedata, fw_type, fw_version, get_averaged_sysref_offset, get_current_timecounter, get_latest_sysref_timecounter, get_names_of_wavedata, get_triggering_awg_to_line, hal, has_wavedata, initialize, initialize_all_awgunits, initialize_awgunits, initialize_sequencer, ipaddr_sss, ipaddr_wss, num_awgunit, num_capmod, num_capunit, num_capunit_of_capmod, register_wavedata, set_triggering_awg_to_line, start_awgunits_now, start_awgunits_timed, start_capunits_by_trigger, start_capunits_now, timecounter_to_second, unset_triggering_awg_to_line
  - 削除: capture_start, clear_before_starting_emission, get_muc_structure, get_num_available_awg, get_num_capunits_of_capmod, hw_lifestage, hw_type, hw_type_and_lifestage, hw_version, initialize_all_awgs, initialize_awgs, is_monitor_shared_with_read, set_cw, set_iq, set_param_awg, set_param_capunit, simple_capture, simple_capture_start, simple_cw_gen, simple_iq_gen, simple_multiple_capture_start, start_emission, stop_emission, validate_installed_e7awgsw
  - 変更: initialize_capunits(旧: (self, capunits)) → (新: (self, capunit_idxs))

## quel_ic_config.quel1se_config_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1se_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1se_config_subsystem.py)
- 追加されたクラス: Ad9082Quel1se, Quel1seConfigSubsystemAd9082Mixin

## quel_ic_config.quel1se_fujitsu11_config_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1se_fujitsu11_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1se_fujitsu11_config_subsystem.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1se_fujitsu11_config_subsystem.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1se_fujitsu11_config_subsystem.py)
- クラス `Quel1seFujitsu11TypeAConfigSubsystem` のメソッド差分:
  - 追加: initialize
- クラス `Quel1seFujitsu11TypeADebugConfigSubsystem` のメソッド差分:
  - 追加: initialize
- クラス `Quel1seFujitsu11TypeBConfigSubsystem` のメソッド差分:
  - 追加: initialize
- クラス `Quel1seFujitsu11TypeBDebugConfigSubsystem` のメソッド差分:
  - 追加: initialize

## quel_ic_config.quel1se_riken8_config_subsystem
- 新: [quel_ic_config/src/quel_ic_config/quel1se_riken8_config_subsystem.py](quel_ic_config/src/quel_ic_config/quel1se_riken8_config_subsystem.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel1se_riken8_config_subsystem.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel1se_riken8_config_subsystem.py)
- 追加されたクラス: ExstickgeCoapClientQuel1seRiken8WithLock
- 削除されたクラス: ExstickgeCoapClientQuel1seRiken8Dev1, ExstickgeCoapClientQuel1seRiken8Dev2
- クラス `ExstickgeCoapClientQuel1seRiken8Dev1` のメソッド差分:
  - 削除: read_boxtype, read_current_config, write_current_config
- クラス `ExstickgeCoapClientQuel1seRiken8Dev2` のメソッド差分:
  - 削除: read_boxtype, read_current_config, write_current_config
- クラス `Quel1seRiken8ConfigSubsystem` のメソッド差分:
  - 追加: initialize
- クラス `Quel1seRiken8DebugConfigSubsystem` のメソッド差分:
  - 追加: initialize

## quel_ic_config.quel_clock_master_v1
- 新: [quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py](quel_ic_config/src/quel_ic_config/quel_clock_master_v1.py)
- 追加されたクラス: QuelClockMasterV1
- クラス `QuelClockMasterV1` のメソッド差分:
  - 追加: check_availability, get_current_timecounter, has_lock, reboot, sync_boxes, terminate

## quel_ic_config.quel_ic
- 新: [quel_ic_config/src/quel_ic_config/quel_ic.py](quel_ic_config/src/quel_ic_config/quel_ic.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/quel_ic.py](v0.8.11/quel_ic_config/src/quel_ic_config/quel_ic.py)
- 追加されたクラス: Ad9082Generic
- 削除されたクラス: Ad9082V106, GenericGpio
- クラス `GenericGpio` のメソッド差分:
  - 削除: read_reg, write_reg

## quel_ic_config.rfswitcharray
- 新: [quel_ic_config/src/quel_ic_config/rfswitcharray.py](quel_ic_config/src/quel_ic_config/rfswitcharray.py)
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/rfswitcharray.py](v0.8.11/quel_ic_config/src/quel_ic_config/rfswitcharray.py)
- 追加されたクラス: QubeRfSwitchArray0Reg, QubeRfSwitchArray1Reg, Quel1TypeARfSwitchArray0Reg, Quel1TypeARfSwitchArray1Reg, Quel1TypeBRfSwitchArray0Reg, Quel1TypeBRfSwitchArray1Reg, RfSwitchArrayReg
- 削除されたクラス: QubeRfSwitchArray0, QubeRfSwitchArray1, Quel1TypeARfSwitchArray0, Quel1TypeARfSwitchArray1, Quel1TypeBRfSwitchArray0, Quel1TypeBRfSwitchArray1, RfSwitchArray
- クラス `QubeRfSwitchArray0` のメソッド差分:
  - 削除: build, parse
- クラス `QubeRfSwitchArray0Reg` のメソッド差分:
  - 追加: build, parse
- クラス `QubeRfSwitchArray1` のメソッド差分:
  - 削除: build, parse
- クラス `QubeRfSwitchArray1Reg` のメソッド差分:
  - 追加: build, parse
- クラス `Quel1TypeARfSwitchArray0` のメソッド差分:
  - 削除: build, parse
- クラス `Quel1TypeARfSwitchArray0Reg` のメソッド差分:
  - 追加: build, parse
- クラス `Quel1TypeARfSwitchArray1` のメソッド差分:
  - 削除: build, parse
- クラス `Quel1TypeARfSwitchArray1Reg` のメソッド差分:
  - 追加: build, parse
- クラス `Quel1TypeBRfSwitchArray0` のメソッド差分:
  - 削除: build, parse
- クラス `Quel1TypeBRfSwitchArray0Reg` のメソッド差分:
  - 追加: build, parse
- クラス `Quel1TypeBRfSwitchArray1` のメソッド差分:
  - 削除: build, parse
- クラス `Quel1TypeBRfSwitchArray1Reg` のメソッド差分:
  - 追加: build, parse

## quel_ic_config.thermistor
- 旧: [v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py](v0.8.11/quel_ic_config/src/quel_ic_config/thermistor.py)
- 削除されたクラス: Quel1NormalThermistor, Quel1PathSelectorThermistor, Quel1seExternalThermistor, Quel1seOnboardThermistor, Thermistor
- クラス `Quel1NormalThermistor` のメソッド差分:
  - 削除: convert
- クラス `Quel1PathSelectorThermistor` のメソッド差分:
  - 削除: convert
- クラス `Quel1seExternalThermistor` のメソッド差分:
  - 削除: convert
- クラス `Quel1seOnboardThermistor` のメソッド差分:
  - 削除: convert
- クラス `Thermistor` のメソッド差分:
  - 削除: convert
