from thunderq.procedures.native import Procedure


class SquareWaveProcedure(Procedure):
    def __init__(self, name, channel, slice, amplitude, duration):
        # arguments explained:
        # - name: the name of this procedure
        # - channel: the channel where this square wave should be performed
        # - slice: the slice where this square wave should be performed
        # - amplitude: the amplitude of this square wave
        # - duration: the duration of this square wave

        super().__init__(name)
        self.channel = channel
        self.slice = slice
        self.amplitude = amplitude
        self.duration = duration

    def pre_run(self):
        # this method is in charge of preparing all waveforms for this procedure,
        # and write them into slices. It will be called before waveforms are
        # written into each channels.

        # create a square wave
        from thunderq.waveforms.native.waveform import DC
        waveform = DC(self.duration, self.amplitude)

        # add this square wave to self.channel at self.slice
        self.slice.add_waveform(self.channel, waveform)

    def post_run(self):
        # this method will be called after one cycle has been done (all waveform
        # in all slices has been written into channels and been performed)

        # for SquareWaveProcedure, it doesn't need to do anything here.
        pass

from thunderq.cycles.native import Cycle

class MultipleSquareWaveCycle(Cycle):
    def __init__(self,square_wave_length, square_wave_amp,
                 channel1, channel2, channel3,channel4,channel5,
                 slice1, slice2, slice3, sequence):
        # sequence: the `sequence` object that holds all channels and slices
        super().__init__("Triple Square Wave Cycle", sequence)
        self.square_wave1 = SquareWaveProcedure("SquareWave1",
                                                channel1,
                                                slice1,
                                                square_wave_amp,
                                                square_wave_length)
        self.add_procedure(self.square_wave1)

        self.square_wave2 = SquareWaveProcedure("SquareWave2",
                                                channel2,
                                                slice2,
                                                square_wave_amp,
                                                square_wave_length)
        self.add_procedure(self.square_wave2)

        self.square_wave3 = SquareWaveProcedure("SquareWave3",
                                                channel3,
                                                slice3,
                                                square_wave_amp,
                                                square_wave_length)
        self.add_procedure(self.square_wave3)

        self.square_wave4=SquareWaveProcedure("SquareWave4",
                                              channel4,
                                              slice1,
                                              square_wave_amp,
                                              square_wave_length,
                                              )
        self.add_procedure(self.square_wave4)

        self.square_wave5=SquareWaveProcedure("SquareWave4",
                                              channel4,
                                              slice2,
                                              square_wave_amp,
                                              square_wave_length,
                                              )
        self.add_procedure(self.square_wave5)

        # self.square_wave6=SquareWaveProcedure("SquareWave4",
        #                                       channel4,
        #                                       slice2,
        #                                       square_wave_amp,
        #                                       square_wave_length,
        #                                       )
        # self.add_procedure(self.square_wave5)

        self.square_wave6=SquareWaveProcedure("SquareWave5",
                                              channel5,
                                              slice2,
                                              square_wave_amp,
                                              square_wave_length,
                                              )
        self.add_procedure(self.square_wave6)

        self.square_wave7=SquareWaveProcedure("SquareWave5",
                                              channel5,
                                              slice3,
                                              square_wave_amp,
                                              square_wave_length,
                                              )
        self.add_procedure(self.square_wave7)






# import channel and trigger wrapper from sequencer

from thunderq.sequencer import AWGChannel, DGTrigger

# import mock devices
from thunderq.helper.mock_devices import MockAWG, MockDG

# create three waveform channels with MockAWG
mock_awg0 = AWGChannel("mock_awg0", MockAWG("mock_awg0"))
mock_awg1 = AWGChannel("mock_awg1", MockAWG("mock_awg1"))
mock_awg2 = AWGChannel("mock_awg2", MockAWG("mock_awg2"))
mock_awg3=AWGChannel("mock_awg3",MockAWG("mock_awg3"))
mock_awg4=AWGChannel("mock_awg4",MockAWG("mock_awg4"))

# create trigger from mock delay generator
mock_dg = DGTrigger(MockDG())

from thunderq.runtime import Runtime

# runtime saves some common components used in an experiment like its sequence,
# the logger, and some configurations, etc.
runtime = Runtime()

# set the frequency of this DG to be 100000 Hz (10us per cycle)
sequence = runtime.create_sequence(mock_dg, 100000)
# set the position of the edge of trigger line 0: to raise at 0 and drop after 1us
sequence.add_trigger("test_trigger_0", 0, 0, 1e-6) \
    .link_waveform_channel("channel_0", mock_awg0) \
    .link_waveform_channel("channel_1", mock_awg1) \
    .link_waveform_channel("channel_2", mock_awg2)\
    .link_waveform_channel("channel_3", mock_awg3)\
    .link_waveform_channel("channel_4", mock_awg4)  # link channels that are triggered by this edge

# define three slices
from thunderq.sequencer import FlexSlice

# FlexSlice doesn't has a fixed start point and length
# it's start point is determined by slices before it, while its length depends
# on the waveform in it.
slice_a = FlexSlice("slice_a")
slice_b = FlexSlice("slice_b")
slice_c = FlexSlice("slice_c")

# add slices into sequence
sequence.add_slice(slice_a)
sequence.add_slice(slice_b)
sequence.add_slice(slice_c)

cycle = MultipleSquareWaveCycle(
    square_wave_length=3e-6,
    square_wave_amp=1,
    channel1=mock_awg0,
    channel2=mock_awg1,
    channel3=mock_awg2,
    channel4=mock_awg3,
    channel5=mock_awg4,
    slice1=slice_a,
    slice2=slice_b,
    slice3=slice_c,
    sequence=sequence)

# run the entire cycle
cycle.run()

sequence.send_sequence_plot(plot_sample_rate=1e9)
