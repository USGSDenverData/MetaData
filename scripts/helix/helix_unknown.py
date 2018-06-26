'''
baseline:
  after: True
  before: False
  counts: 60
  detector: H2
  mass: 39.59
default_fits: nominal
equilibration:
  eqtime: 90
  inlet: "2"
  inlet_delay: 3
  outlet: "1"
  use_extraction_eqtime: false
multicollect:
  counts: 120
  detector: H2
  isotope: Ar40
peakcenter:
  after: true
  before: false
  detector: H2
  isotope: Ar40
peakhop:
  hops_name: hop
  use_peak_hop: false
'''

DETECTORS=['H2','H1','AX', 'L1', 'L2(CDD)']

def main():
    activate_detectors(*DETECTORS)

    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)
    if mx.equilibration.use_extraction_eqtime:
        eq = ex.eqtime
    else:
        eq = mx.equilibration.eqtime

    equilibrate(eqtime=eq, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)
    set_time_zero()
    sniff(eq)

    set_fits()
    set_baseline_fits()

    multicollect(ncounts=mx.multicollect.counts)
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts, mass=mx.baseline.mass, detector=mx.baseline.detector)
    if mx.peakcenter.after:
        peak_center(detector=mx.peakcenter.detector, isotope=mx.peakcenter.isotope)
