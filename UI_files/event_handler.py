class event_handler:
    def __init__(self, ui, basic_funcs, funcs):
        # counter = basic_funcs['counter']
        confocal = basic_funcs['confocal']
        B_align = basic_funcs['B_align']
        spin_control = funcs['spin_control']
        # T1_sensing = funcs['T1_sensing']
        resonant = funcs['resonant']
        # attocube = funcs['attocube']
        entanglement = funcs['entanglement']
        ############# main ##############
        ui.btn_1_confocal.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
        ui.btn_2_magnet.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
        ui.btn_3_control.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
        ui.btn_4_PLE.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))
        ui.btn_5_entangle.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(4))
        ui.btn_6_T1.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(5))
        
        ########### confocal ###########
        ui.x_fix.clicked.connect(lambda: confocal.x_fix())
        ui.y_fix.clicked.connect(lambda: confocal.y_fix())
        ui.z_fix.clicked.connect(lambda: confocal.z_fix())
        ui.confocal_home.clicked.connect(lambda: confocal.go_home())
        ui.confocal_moveto.clicked.connect(lambda: confocal.pressedMove())
        ui.confocal_start.clicked.connect(lambda: confocal.start())
        ui.verticalSlider_2.valueChanged.connect(lambda: confocal.slided())
        ui.counter_laser_on.clicked.connect(lambda: confocal.pushButton_laser())
        ui.counter_laser_on_2.clicked.connect(lambda: confocal.pushButton_red1_laser())
        ui.counter_laser_on_3.clicked.connect(lambda: confocal.pushButton_red2_laser())
        ui.counter_start.clicked.connect(lambda: confocal.counter_start())
        ui.pushButton_AutoAlign_red.clicked.connect(lambda: confocal.pushButton_autoAlign_red())
        ui.pushButton_AutoAlign_zpl.clicked.connect(lambda: confocal.pushButton_autoAlign_zpl())
        ui.pushButton_pulse_gen.clicked.connect(lambda: confocal.pushButton_pulse_gen())
        
        ########### autofocus ###########
        ui.autofocus_001.clicked.connect(lambda: confocal.T_001())
        ui.autofocus_005.clicked.connect(lambda: confocal.T_005())
        ui.autofocus_01.clicked.connect(lambda: confocal.T_01())
        ui.autofocus_start.clicked.connect(lambda: confocal.start_autofocus())
        
        ########### spin control ##########
        ui.control_start.clicked.connect(lambda: spin_control.start())
        # ui.control_params.clicked.connect(lambda: spin_control.params())
        ui.control_stop.clicked.connect(lambda: spin_control.stop())
        ui.control_fitting.stateChanged.connect(lambda: spin_control.fit_state_changed())
        
        ########### B_align ############
        ui.magnet_moveto.clicked.connect(lambda: B_align.move())
        ui.magnet_jog_foward_x.clicked.connect(lambda: B_align.jog(ui.magnet_jog_foward_x))
        ui.magnet_jog_foward_y.clicked.connect(lambda: B_align.jog(ui.magnet_jog_foward_y))
        ui.magnet_jog_foward_z.clicked.connect(lambda: B_align.jog(ui.magnet_jog_foward_z))
        ui.magnet_jog_backward_x.clicked.connect(lambda: B_align.jog(ui.magnet_jog_backward_x))
        ui.magnet_jog_backward_y.clicked.connect(lambda: B_align.jog(ui.magnet_jog_backward_y))
        ui.magnet_jog_backward_z.clicked.connect(lambda: B_align.jog(ui.magnet_jog_backward_z))
        ui.magnet_start.clicked.connect(lambda: B_align.start())
        
        ######### Resonant ##############
        ui.pushButton_CH1_connect.clicked.connect(lambda: resonant.pressed_connect_CH1())
        ui.pushButton_CH2_connect.clicked.connect(lambda: resonant.pressed_connect_CH2())
        ui.pushButton_laserlock_button_1.clicked.connect(lambda: resonant.pressed_laserLock_CH1())
        ui.pushButton_laserlock_button_2.clicked.connect(lambda: resonant.pressed_laserLock_CH2())
        ui.pushButton_PLE_start.clicked.connect(lambda: resonant.pressed_PLE_start())
        ui.pushButton_wavelength_scan_start.clicked.connect(lambda: resonant.pressed_WL_scan_start())
        ui.pushButton_change_wavelength_1.clicked.connect(lambda: resonant.pressed_change_wl_CH1())
        ui.pushButton_PLE_repeat.clicked.connect(lambda: resonant.pressed_PLE_repeat())

        ####### entanglement ########
        ui.pushButton_spin_photon_start.clicked.connect(lambda: entanglement.pressed_spinPhoton_button())