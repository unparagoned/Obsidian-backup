---
title: "Wearable device-based health equivalence of different physical activity intensities against mortality, cardiometabolic disease, and cancer - Nature Communications"
source: "https://www.nature.com/articles/s41467-025-63475-2"
author:
  - "[[Raaj Kishore Biswas]]"
  - "[[Matthew N. Ahmadi]]"
  - "[[Adrian Bauman]]"
  - "[[Karen Milton]]"
  - "[[Nicholas A. Koemel]]"
  - "[[Emmanuel Stamatakis]]"
published: 2025-10-07
created: 2026-01-17
description: "Current conventions, partly derived from self-reported data, typically equate 1 minute of vigorous physical activity (VPA) to 2 minutes of moderate physical activity (MPA). Using accelerometer-derived intensity classification in 73,485 UK Biobank participants (mean follow-up: 8.0 [1.0] years), we assess the equivalence of light activity (LPA) and MPA to 1 minute of VPA for all-cause (ACM) and cardiovascular (CVD) mortality, major adverse cardiovascular events (MACE), type 2 diabetes, and cancer outcomes. For a standardised 5%–35% risk reduction, the median MPA equivalent per minute of VPA is 4.1 (ACM, 95% CI: 4.1–4.2), 7.8 (CVD mortality, 7.7-8.0), 5.4 (MACE, 5.3–5.5), 9.4 (type 2 diabetes, 9.3-9.6), and 3.5 (cancer mortality, 3.4-3.5) minutes. For non-cancer outcomes, the median LPA equivalent per 1 minute of VPA ranges from 53 (ACM) to 94 minutes (type 2 diabetes), reflecting generally weaker dose-response curves of LPA with all outcomes. These findings indicate a substantial departure from self-reported estimates and support integrating device-based equivalence into guidelines and wearables. Benefits on health have been found to vary across different levels of physical activity (PA) for chronic conditions including cancer. Here the authors report that each minute of vigorous intensity PA is equivalent to various minutes of moderate and light PA in terms of all-cause, cardiometabolic disease and cancer mortality outcomes in a device-based population."
tags:
  - "clippings"
---
## Abstract

Current conventions, partly derived from self-reported data, typically equate 1 minute of vigorous physical activity (VPA) to 2 minutes of moderate physical activity (MPA). Using accelerometer-derived intensity classification in 73,485 UK Biobank participants (mean follow-up: 8.0 \[1.0\] years), we assess the equivalence of light activity (LPA) and MPA to 1 minute of VPA for all-cause (ACM) and cardiovascular (CVD) mortality, major adverse cardiovascular events (MACE), type 2 diabetes, and cancer outcomes. For a standardised 5%–35% risk reduction, the median MPA equivalent per minute of VPA is 4.1 (ACM, 95% CI: 4.1–4.2), 7.8 (CVD mortality, 7.7-8.0), 5.4 (MACE, 5.3–5.5), 9.4 (type 2 diabetes, 9.3-9.6), and 3.5 (cancer mortality, 3.4-3.5) minutes. For non-cancer outcomes, the median LPA equivalent per 1 minute of VPA ranges from 53 (ACM) to 94 minutes (type 2 diabetes), reflecting generally weaker dose-response curves of LPA with all outcomes. These findings indicate a substantial departure from self-reported estimates and support integrating device-based equivalence into guidelines and wearables.

## Introduction

The benefits of physical activity are well established for both the general population and for specific clinical subgroups [^1] [^2]. There is a clear dose-response relationship between physical activity intensity and mortality or non-communicable disease risk reduction [^1] [^3] [^4]. Based on such evidence, the current WHO physical activity guidelines recommend that all adults accumulate 150–300 min of moderate-intensity physical activity (MPA) or 75–150 min of vigorous physical activity (VPA) per week or an equivalent combination of moderate and vigorous activities [^1]. This recommendation is primarily based on epidemiological evidence from self-reports, such as questionnaires [^5] [^6], where each minute of vigorous activity is given twice the weight of moderate-intensity activities, representing a 1:2 ratio. This convention is based on metabolic equivalent (MET) values whereby each vigorous activity (>6 MET) [^7] requires, on average, about twice the energy expenditure of moderate activities (3–6 MET) [^7]. Studies examining the associations of physical activity volume with mortality and other long term health outcomes [^8] [^9] have thus assumed that 1 min of vigorous activity produces similar benefits to around 2 min of moderate activity. However, this is non-empirically derived and has not been objectively tested on a population level despite the emergence of highly granular wearables data in health research. Additionally, no studies have compared light intensity with moderate or vigorous activity to determine their equivalence.

Recent device measured studies have demonstrated that vigorous activity may be considerably more time efficient than moderate or light intensity activities in producing cardiovascular and metabolic adaptations [^10] [^11], a finding that is also reflected by epidemiological studies examining the associations of vigorous activity with CVD and mortality [^4] [^12] [^13]. These studies indicate that there may be lower time commitment and convenience benefits for structured and intermittent vigorous activities for both patients and healthy populations, although vigorous exertion may cause discomfort and pose adherence challenges in people who are not accustomed to it [^14]. To expand intervention options, further work is needed to specifically quantify the “health value” of activities of different intensity levels against key health outcomes.

Fewer studies have examined if light-intensity physical activity (LPA) is associated with prospective health outcomes [^15], in part due to the inability of self-reported instruments to capture light intensity activity [^16] [^17]. Systematic reviews indicate some potential for reducing all-cause mortality risk from light intensity activity, and randomized controlled trials show improvements in glycemic control and other metabolic parameters [^18] [^19]. The few studies that used devices to quantify the association of LPA with mortality or cardiovascular disease show mixed findings, and none estimated specifically its per-time unit equivalence to vigorous intensity [^15] [^20] [^21].

Using algorithms that are partly based on existing, less empirical, research standards [^3] [^8] [^9], consumer grade wearables commonly assign a “health value” to each minute of physical activity the wearable device records, to support setting and monitoring physical activity goals [^22] [^23], e.g., Google Fit Heart Points and Apple Fitness+ [^22] [^23]. For example, Google Fit assigns Heart Points based on the intensity of the activity: 1 heart point if it is moderate intensity (100–130 steps per minute) and 2 heart points if it is vigorous (>130 steps per minute) [^24]. In the absence of published epidemiological studies estimating the equivalence of wearable device-measured physical activity intensity, it is highly unlikely that any consumer-grade algorithms reflect the associations of intensity with long term clinical and mortality endpoints when calculating these metrics.

In this work, we used a large device-based population cohort and a validated two-stage machine learning-based intensity classification schema to examine the equivalence of light and moderate intensity against each minute of vigorous intensity against a range of key mortality, cardiometabolic, and cancer related outcomes. Each minute of vigorous intensity activity is roughly equivalent to 4–9 min of moderate and 53–156 min of light intensity physical activity, suggesting a considerable departure from previous self-reported evidence conventions. These findings support the incorporation of device-based health equivalence estimates into future physical activity guidelines and the algorithms used in consumer-grade wearables.

## Results

### Cohort information

The UK Biobank is a prospective cohort study involving adults aged 40–69 at baseline (2006–10). At baseline, the mean age of participants was 61.6 years (SD 7.9), 41,420 (56.4%) were women and 32,065 (43.6%) were men.

From 2013 to 2015, a total of 103,684 UK Biobank participants wore a wrist-worn accelerometer on their dominant wrist for 24 h a day over a period of 7 days [^25], in line with previous studies [^12] [^13]. Our analysis included participants who had a minimum of 3 valid wear days (≥16 h of wear-time per day), with at least one of those days being a weekend day. We excluded those with insufficient valid wear days, missing covariate data, or who reported an inability to walk. Supplementary Fig. [1](https://www.nature.com/articles/s41467-025-63475-2#MOESM1) provides a flow diagram of the study participants. We followed the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) reporting guideline (Supplementary Data  [4](https://www.nature.com/articles/s41467-025-63475-2#MOESM5)).

Our analytic sample included 73,485 participants with 2675 all-cause mortality events, 545 CVD mortality events, 2359 MACE events, 1836 type-2 diabetes events, 538 physical activity related cancer mortality events, and 2662 physical activity related cancer incidence events. Supplementary Data [1](https://www.nature.com/articles/s41467-025-63475-2#MOESM2) shows participant characteristics by levels of VPA duration. The mean age of participants was 61.6 (7.9) years and mean follow-up was 8.0 (1.0) years, corresponding to 585,313 (ACM), 538,708 (CVD mortality), 531,656 (MACE), 564,048 (type 2 diabetes), 551,512 (physical activity related cancer mortality), and 541,893 (physical activity related cancer incidence) person-years.

### Dose-response associations of intensity-specific physical activity

Supplementary Fig. [2](https://www.nature.com/articles/s41467-025-63475-2#MOESM1) illustrates the adjusted dose-response relationships for VPA, MPA, and LPA after mutual and multivariable adjustments. Compared to the referent (VPA and MPA: 0 min/day; LPA: 37.9 min/day), both VPA and MPA demonstrated favourable dose-response associations across all outcomes, whereas LPA exhibited a slight risk reduction for type 2 diabetes and ACM only. Specifically, VPA displayed pronounced dose-response gradients for all outcomes, exhibiting nearly linear associations for ACM, CVD mortality, MACE, and type 2 diabetes, with hazard ratios reaching 50% or higher. MPA showed a steep inverse dose-response relationship with all outcomes up to around 30 min per day. In contrast, LPA demonstrated a subtle gradient with type 2 diabetes and ACM, with no statistically significant associations observed for any other outcomes.

### Equivalence of different physical activity intensities

Supplementary Data [2](https://www.nature.com/articles/s41467-025-63475-2#MOESM3) and [3](https://www.nature.com/articles/s41467-025-63475-2#MOESM4) presents the risk reduction for all six outcomes, in 5% increments for each physical activity intensity. Figures  [1](https://www.nature.com/articles/s41467-025-63475-2#Fig1) and [2](https://www.nature.com/articles/s41467-025-63475-2#Fig2) describe the equivalent minutes of MPA and LPA relative to each minute of VPA for risk reduction within the range of 5–35% (hazard ratio: 0.95–0.65) through continuous increments.

![figure 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-63475-2/MediaObjects/41467_2025_63475_Fig1_HTML.png?as=webp)

Fig. 1: Equivalence of moderate (MPA) intensity time against 1 min of vigorous intensity physical activity (VPA) by increments of risk reduction in all-cause mortality, major adverse cardiovascular events (MACE), CVD mortality, type 2 diabetes, physical activity related cancer mortality and physical activity related cancer incidence.

We observed a wide range of equivalence between MPA and VPA across outcomes. The median equivalence of MPA per minute of VPA was 4.1 (95% CI: 4.1–4.2) minutes for ACM, 7.8 (7.7–8.0) minutes for CVD mortality, 5.4 (5.3–5.5) minutes for MACE, and 9.3 (9.3–9.6) minutes type 2 diabetes. The VPA:MPA equivalence curve (Fig. [1](https://www.nature.com/articles/s41467-025-63475-2#Fig1)) remained stable for ACM, MACE, and CVD mortality, while the curve for type 2 diabetes shifted upwards for higher levels of risk reduction (>25%). The median MPA equivalence for each minute of VPA was 6.6 min for ACM, CVD mortality, MACE, and type 2 diabetes. For physical activity related cancer mortality and incidence, the dose-response association was weaker than other outcomes (Supplementary Fig. [2](https://www.nature.com/articles/s41467-025-63475-2#MOESM1)), as a result the equivalence between VPA and MPA was lower, with ratios of 1 to 3.5 for physical activity related cancer mortality and 1 to 1.6 for physical activity related cancer incidence.

In contrast to MPA, the LPA to VPA equivalence exhibited considerable variability across different levels of risk reduction (Supplementary Data [2](https://www.nature.com/articles/s41467-025-63475-2#MOESM3) – [3](https://www.nature.com/articles/s41467-025-63475-2#MOESM4) and Fig. [2](https://www.nature.com/articles/s41467-025-63475-2#Fig2)). For non-cancer outcomes the median equivalence of LPA per minute of VPA ranged from 53 (ACM) to 92 minutes (type 2 diabetes). For ACM we observed an equivalence of 52.6 (51.9-53.5) minutes of LPA for every 1 min of VPA, 72.5 (71.7–73.7) minutes for CVD mortality, 86.1 (84.4-87.9) minutes for MACE and 94.0 (92.3–95.3) minutes for type 2 diabetes. The median LPA equivalence for each minute of VPA was 79.3 min for ACM, CVD mortality, MACE, and type 2 diabetes. Due to the weak dose-response association of LPA with physical activity-related cancer outcomes, the equivalence with VPA was also markedly different to other outcomes (e.g., 1 min of vigorous to a median of 156.2 (153.3–159.3) minutes of LPA for physical activity related cancer mortality, Supplementary Data  [3](https://www.nature.com/articles/s41467-025-63475-2#MOESM4) and Fig. [2](https://www.nature.com/articles/s41467-025-63475-2#Fig2)). Using the same dose response data, we further derived the per MPA minute equivalence of LPA in terms of MPA by dividing the VPA-to-LPA and VPA-to-MPA ratios (Table  [1](https://www.nature.com/articles/s41467-025-63475-2#Tab1)**)**. In summary, the median LPA equivalence per 1 min of MPA ranged from 3.1 min (physical activity related cancer incidence), to 1:9.3 min (CVD mortality), 10.0 min (type 2 diabetes), 12.9 min (ACM), 15.8 min (MACE), and 45.0 min (physical activity related cancer mortality).

![figure 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-63475-2/MediaObjects/41467_2025_63475_Fig2_HTML.png?as=webp)

Fig. 2: Equivalence of light (LPA) intensity time against 1 min of vigorous intensity physical activity (VPA) by increments of risk reduction in all-cause mortality, major adverse cardiovascular events (MACE), CVD mortality, type 2 diabetes, physical activity related cancer mortality and physical activity related cancer incidence.

**Table 1 Summary of median equivalence against the study outcomes across all three intensity bands (*N*  = 73,485)**

## Discussion

This large-scale study of 73,485 adults, aged 40 to 79 years at accelerometry baseline, provides, to our knowledge, the first examination of physical activity intensity equivalence with a broad range of major outcomes including all-cause, cardiovascular, and cancer mortality. We found 1-min of vigorous intensity physical activity was equivalent to about 4–9 min of moderate intensity and 53–156 min of light intensity for all-cause mortality and cardiometabolic outcomes (MACE, type 2 diabetes, and CVD mortality). Our findings are in stark contrast to the widely used current convention of a 1:2 ratio between vigorous and moderate intensity, which was derived from self-reported data. Using a wide array of mortality and major non-communicable disease end points, our study is the first to systematically quantify the equivalence between LPA, MPA, and VPA various intensities of physical activity for use in public health and prevention research, as well as in consumer-grade wearable devices. Our work expands behaviour change options by indicating alternatives to higher intensities, informs the development of physical activity guidelines based on wearable devices, enhances surveillance measures, and supports practitioners and future trials to establish more accurate dosages and define options for prescribing physical activity prescription and personalised medicine initiatives.

For all-cause mortality, we observed a consistent equivalence ratio of 1:4 for vigorous intensity to moderate intensity when the inverse dose-response association ranged between 5% to 35% lower mortality. For cause-specific mortality of CVD and cancer, the equivalence ratio was slightly stronger, where we observed a consistent ratio of 1:8 and 1:3.5 for vigorous intensity to moderate intensity. These findings suggest a 2–4 times stronger potential health effect for vigorous intensity minutes than previously observed in cohort studies reliant on self-report [^26] [^27] [^28]. The discrepancy in our findings compared to traditional self-report evidence is likely due to the higher precision afforded by the continuous and highly granular (10 s epochs) physical activity estimation provided by our wearable data methodology [^4] [^12] [^13], which enabled us to quantify the time spent in different intensity ranges. Self-report methods rely on participants recalling blocks of time spent in moderate to vigorous activities (usually structured exercise) that last above a certain minimum duration threshold, typically 10 to 15 minutes and over [^29]. This can lead to various biases, such as regression dilution bias [^30], and reflects the inherent imprecision of such measurements. The previously recommended 1:2 ratio between vigorous and moderate intensity is likely the result of such limitations of self-reports [^10].

Our equivalence findings between vigorous and moderate intensity are broadly consistent with randomised controlled trials and cross-sectional studies. Previous works that have compared vigorous intensity to moderate intensity activities and exercise under supervised and controlled clinic conditions [^31] [^32] [^33] [^34] [^35] demonstrated an approximate 1:7 to 1:13 ratio for surrogate cardiometabolic outcomes such as lipid profile, blood pressure, and cardiorespiratory fitness [^31] [^36] [^37] [^38] [^39]. Our results expand this evidence with long-term clinical endpoints and mortality in a real-world population cohort measured in environments outside controlled clinic conditions. Our findings at the population level alongside those of smaller RCTs under controlled conditions provides evidence that may improve future public health messaging and programs. Taken together, our findings prompt some reinterpretation of the physical activity evidence-base, particularly in regard to current guidelines suggesting 75–150 min of vigorous intensity is equivalent to 150–300 min of moderate intensity, reflecting the traditional 1:2 ratio between vigorous and moderate intensity.

We observed an equivalence ratio of 1:53 for vigorous intensity to light intensity for all-cause mortality and a ratio of 1:73 for cardiovascular and 1:156 for cancer mortality. Due to the inability of questionnaires to capture light intensity activities, device-based assessment provides the first direct examination of light intensity time equivalence. Although light intensity is accumulated in higher volumes throughout a standard day, our findings highlight the time efficiency of vigorous activity, with requiring 1–2 h of light intensity activity to derive analogous associations as 1 min of vigorous intensity. In addition, for all outcomes, light intensity did not lower risk to an equivalent dose-response association beyond 15% for ACM, MACE, and type 2 diabetes, and 10% for physical activity related cancer. These findings are particularly relevant for adults at high risk of disease, or those who are time poor, and suggest different health promotion strategies. For example, exercising at different intensities or completing light intensity daily activities such as household tasks, stair climbing, or light strolling could be interspersed with short bursts [^13] [^32] of fast walking for a more impactful physical activity session. Our findings provide clinicians with essential information for selecting intervention options to support physical activity behaviour change in patients or individuals at high risk of major lifestyle-related chronic diseases. Specifically, consumer wearable devices that provide activity feedback may facilitate behaviour change, and understanding how accumulation across different activity intensities can be used to tailor treatment.

The prolonged times spent in light intensity activity in this cohort, and the weak dose-response association we observed, are relatively consistent with prior device-based studies and meta-analyses that have examined light intensity [^15] [^20] [^33] [^34]. Prior examinations of bias effects in population cohorts have found light intensity activity is more prone to reverse causation than higher intensity activities [^35]. The precautions we took to mitigate the influence of such bias in our analyses may explain, in part, the observed weaker dose-response associations of light intensity compared to other studies [^40] [^41] that found a protective association [^42] [^43].

The equivalence estimates are derived from predicted hazard ratios (HRs) across different intensity bands, using a single Fine-Gray subdistribution hazard model for each disease outcome. To quantify uncertainty around these estimates, we applied a bootstrapping approach to the predicted values. This generated confidence intervals that represent the variability inherent in the model-based predictions. It is important to note that these confidence intervals are not intended to serve as indicators of statistical significance. Rather, they are presented to illustrate the range of plausible equivalence estimates based on the model’s assumptions and sampling variability. They should not be interpreted as indicators of statistical significance.

Strengths of our study include the use of wearables to quantify physical activity at a high granularity in the largest resource to date with linkage to prospective health outcomes. We examined a spectrum of conditions responsible for much of the burden of non-communicable disease, encompassing both incidence and mortality, to explore equivalence across specific categories of physical activity intensity. The large sample size and long follow up allowed us to reduce the risk of reverse causality by removing participants who had an event within the initial 12 months of follow-up or prevalent disease at baseline. Despite the extensive precautionary measures, the potential for our equivalence estimates to reflect a degree of reverse causation may still exist, for example low activity levels due to undiagnosed or prodromal disease [^35] [^44]. Due to the observational design, we cannot rule out the presence of unmeasured confounding. However, our adjustment for potential confounders was based on previously established cause-effect pathways between physical activity and non-communicable disease that informed our direct acyclic graph. The wearables used in the UK Biobank relied on accelerometers quantifying absolute intensity, not energy expenditure. Previous research, however, has indicated that adjusting absolute intensity for participant characteristics that determine energy expenditure (weight, height, age, and sex), does not materially influence the association of physical activity volume with cause-specific and overall mortality [^40]. The median time gap between the UK Biobank baseline, when covariate measurements were collected, and the accelerometry study was 5.5 years. However, most covariates remained stable over this period, with the exception of medication use [^13]. The UK Biobank had a very low response rate (5.5%), and participants in our sample were subject to additional selection criteria which should be considered when interpreting our results. However, evidence suggests that, at least with mortality endpoints, low response rates, and the subsequent unrepresentativeness to the target population, does not materially affect estimates of the association of physical activity [^41].

Our study represents the first device-based evidence on the health equivalence of different physical activity intensities. Our findings reveal a distinctively higher equivalence for moderate intensity compared to the previous convention based on self-reported data, which equates one minute of vigorous intensity to 2 min of moderate intensity, as reflected in current guidelines [^1] [^45] [^46]. Each minute of vigorous activity is associated with risk reduction levels comparable to 4–9 min of moderate intensity; and 53–156 min of light intensity physical activity - while acknowledging that not even the largest amounts of daily LPA can elicit the beneficial effects of moderate or vigorous intensities. Our findings inform future guidelines and lifestyle interventions, and can help improve the algorithms used in consumer-grade wearables to quantify the health benefits of each minute of physical activity or exercise.

## Methods

### Physical activity assessment and exposure variables

The data were calibrated, and non-wear periods were identified according to standard procedures [^47] [^48]. Non-wear periods were identified using the signal standard deviation to detect periods where the standard deviation was below 0.13 milligravity for 30 or more minutes, reflecting non-wear. Sleep was detected based on relative changes in wrist tilt angle.

We categorised physical activity intensities into LPA, MPA and VPA using a validated two-stage machine learning-based Random Forest activity classifier [^4] [^13]. We have described the physical activity intensity classification schema in detail elsewhere [^12] [^13] [^32] and we include here as Supplementary text (including Supplementary Figs. [3](https://www.nature.com/articles/s41467-025-63475-2#MOESM1) – [4](https://www.nature.com/articles/s41467-025-63475-2#MOESM1) and Supplementary Tables  [7](https://www.nature.com/articles/s41467-025-63475-2#MOESM1) – [8](https://www.nature.com/articles/s41467-025-63475-2#MOESM1)). In summary, this 2-stage machine learning-based Random Forest activity classifier uses raw acceleration signals to identify and quantify time spent in different activity types and intensities in 10 s windows.

### Mortality and disease endpoints

Definitions of outcomes along with disease specific International Classification of Diseases codes are provided in Supplementary Table [5](https://www.nature.com/articles/s41467-025-63475-2#MOESM1). In addition to all-cause mortality (ACM), five other outcomes were derived: CVD mortality, major adverse cardiovascular events (MACE), type 2 diabetes, physical activity related cancer mortality and incidence. CVD was defined as diseases of the circulatory system, excluding hypertension, diseases of arteries, and lymph. MACE was defined as CVD death or incidents of myocardial infarction, stroke, and heart failure. Incidents of type 2 diabetes was extracted from hospitalisation and general practitioner records. Physical activity related cancer encompasses various cancer types associated with increased levels of physical activity, excluding in situ, benign, uncertain, non-melanoma skin cancer, or non-well-defined cancers [^49]. The selected cancer types were informed by prior meta-analyses and pooled studies that demonstrated significant or suggestive associations between physical activity and cancer risk, see detailed list of cancer ICD-10 codes in Supplementary Table  [5](https://www.nature.com/articles/s41467-025-63475-2#MOESM1).

### Events ascertainment

Participants were followed up through November 30 <sup>th</sup>, 2022, with deaths obtained via linkage with the National Health Service (NHS) Digital of England and Wales or the NHS Central Register and National Records of Scotland. Inpatient hospitalisation data were provided by either the Hospital Episode Statistics for England, the Patient Episode Database for Wales, or the Scottish Morbidity Record for Scotland. Cancer data linkage was obtained through national cancer registries. For England and Wales, cancer diagnosis data were followed up through 31 December 2020 and 31 December 2016 respectively, and were provided by NHS England [^50]. For Scotland, cancer diagnosis data were followed up through 30 November 2021 and provided by the National Records of Scotland [^50].

### Inclusion criteria

We followed established inclusion criteria from analogous analyses [^4] [^12] [^13] [^32]. For each outcome, participants with a prior diagnosis of the respective condition by the time the accelerometry baseline started were excluded. Adjustments in the models primarily accounted for cardiovascular disease (CVD) and cancer, as these are the leading causes of mortality. Specifically, analyses for all-cause mortality (ACM) and type 2 diabetes were adjusted for prior diagnoses of cancer and CVD. For major adverse cardiovascular events (MACE) and other CVD outcomes, prior cancer incidence was considered, while analyses for cancer outcomes were adjusted for previous CVD diagnoses.

### Statistics and reproducibility

To reduce the risk of reverse causation due to undiagnosed disease, individuals registering an event within the initial 12 months of follow-up were excluded from diseases specific analyses [^4] [^32]. We also excluded those with prevalent diseases at baseline accelerometry assessment [^4] [^13] [^32]. The upper range of all three physical activity intensity-specific categories was winsorized at the 97.5 <sup>th</sup> percentile to alleviate the impact of sparse data or outliers [^4] [^13] [^32].

We investigated the time-to-event dose-response associations of intensity-specific categories with the six outcomes. For these analyses, we calculated hazard ratios (HRs) using Cox proportional hazards for ACM, and Fine-Gray sub-distribution hazard models for all disease-specific outcomes to account for competing risks from deaths not attributed to the analytic outcome [^51]. Knots were placed at the 10 <sup>th</sup>, 50 <sup>th</sup> and 90 <sup>th</sup> percentiles [^52]. Departure from linearity was assessed by a Wald test. Proportional hazards assumptions were tested using Schoenfeld Residuals in the models and no violations were observed (all *p*  > 0.05).

In line with previous analogous analyses [^4] [^12] [^13] [^32], core analyses were adjusted for sex, age, education, ethnicity, fruit and vegetable consumption, smoking history, alcohol consumption, sleep duration, discretionary screentime, CVD related medication use (insulin, blood pressure, cholesterol) and family history of cancer and CVD. Each physical activity intensity-specific spline model was mutually adjusted for physical activity energy expenditure-based volume from other intensities, for example the vigorous activity splines were adjusted for energy expenditure-based volume of moderate and light intensity activity. Referent data point was set to the minimum for all three intensity-specific splines (0 min for VPA and MPA, and 37.9 min for LPA) [^20] [^53]. Complete covariate definitions are provided in Supplementary Data  [6](https://www.nature.com/articles/s41467-025-63475-2#MOESM7).

For estimating equivalence across the three physical activity intensity-specific categories, we extracted the hazard ratios from the Cox/Fine-Gray sub-distribution models. We compared the intensity values within the 5–35% risk reduction range based on the observed relative uniformity in the shape of the dose response curves. An additional reason this range was chosen was that it represents a meaningful spectrum of risk reduction observed across most intensity bands and the selected outcomes. For example, for any given percentage risk reduction in ACM, the hazards of VPA were compared with the same percentage reduction of MPA and LPA. Subsequently, the risk-specific MPA/LPA values (in minutes) were standardized by dividing them by the corresponding VPA values, thereby equating MPA and LPA to one minute of VPA. We calculated 95% confidence intervals through non-parametric bootstrapping of the model-predicted values using 1000 resamples. For each resample, the outcome variable was estimated at rounded predicted risk levels (e.g., 0.65, 0.70,…, 0.95), and the 2.5th and 97.5th percentiles of the resulting bootstrap distributions were used to derive the confidence bounds [^4] [^54].

We conducted all analyses using R statistical software (*version 4.2.3*), employing the RMS (*version 6.3.0*) and survival packages (*version 3.5.5*). Our reporting adheres to the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) guidelines **(**Supplementary Data [4](https://www.nature.com/articles/s41467-025-63475-2#MOESM5)**)**.

### Ethics approval

Participants gave informed consent, and ethical approval was granted by the National Health Service’s National Research Ethics Service in the UK (Ref: 11/NW/0382).

### Reporting summary

Further information on research design is available in the [Nature Portfolio Reporting Summary](https://www.nature.com/articles/s41467-025-63475-2#MOESM8) linked to this article.

## Data availability

The data that support the findings of this study are available from the UK Biobank, but restrictions apply to the availability of these data, which were used under license for the current study, and so are not publicly available. The UK Biobank data that support the findings of this study can be accessed by researchers on application ([https://www.ukbiobank.ac.uk/register-apply/](https://www.ukbiobank.ac.uk/register-apply/)). [Source data](https://www.nature.com/articles/s41467-025-63475-2#Sec15) are provided with this paper.

## Code availability

The statistical code used in the analyses of this manuscript is available upon reasonable request.

## Change history

- ### 30 October 2025
	A Correction to this paper has been published: [https://doi.org/10.1038/s41467-025-65754-4](https://doi.org/10.1038/s41467-025-65754-4)

## References

## Acknowledgements

This research has been conducted using the UK Biobank Resource under Application Number 25813. The authors would like to thank all the participants and professionals contributing to the UK Biobank. This research used data assets made available by National Safe Haven as part of the Data and Connectivity National Core Study, led by Health Data Research UK in partnership with the Office for National Statistics and funded by UK Research and Innovation. This work uses data provided by patients and collected by the NHS as part of their care and support. This study is funded by an Australian National Health and Medical Research Council (NHMRC) Investigator Grant (APP 1194510). The funder had no specific role in any of the following study aspects: the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

## Ethics declarations

### Competing interests

E.S. is a paid consultant and holds equity in Complement 1, a US-based company whose services relate to physical activity. All other authors disclose no conflict of interest for this work.

## Peer review

### Peer review information

*Nature Communications* thanks Jamie Faro and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Supplementary information

### Supplementary Information

### Supplementary Data 1

### Supplementary Data 2

### Supplementary Data 3

### Supplementary Data 4

### Supplementary Data 5

### Supplementary Data 6

### Reporting Summary

### Transparent Peer Review file

## Source data

### Source Data

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

[^1]: Bull, F. C. et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. *Br. J. Sports Med.***54**, 1451–1462 (2020).

[^2]: Chastin, S. F. M. et al. Effects of regular physical activity on the immune system, vaccination and risk of community-acquired infectious disease in the general population: systematic review and meta-analysis. *Sports Med*. **51**, 1673–1686 (2021).

[^3]: Wang, Y., Nie, J., Ferrari, G., Rey-Lopez, J. P. & Rezende, L. F. M. Association of physical activity intensity with mortality. *JAMA Intern Med.***181**, 203 (2021).

[^4]: Ahmadi, M. N. et al. Vigorous physical activity, incident heart disease, and cancer: how little is enough? *Eur. Heart J.***43**, 4801–4814 (2022).

[^5]: Strain, T. et al. Wearable-device-measured physical activity and future health risk. *Nat. Med.***26**, 1385–1391 (2020).

[^6]: Gill, J. M. et al. Potential impact of wearables on physical activity guidelines and interventions: opportunities and challenges. *Br. J. Sports Med.***57**, 1223–1225 (2023).

[^7]: Herrmann, S. D. et al. 2024 adult compendium of physical activities: a third update of the energy costs of human activities. *J. Sport Health Sci.***13**, 6–12 (2024).

[^8]: Rey Lopez, J. P., Sabag, A., Martinez Juan, M., Rezende, L. F. M. & Pastor-Valero, M. Do vigorous-intensity and moderate-intensity physical activities reduce mortality to the same extent? A systematic review and meta-analysis. *BMJ Open Sport Exerc. Med.***6**, e000775 (2020).

[^9]: Rey Lopez, J. P., Gebel, K., Chia, D. & Stamatakis, E. Associations of vigorous physical activity with all-cause, cardiovascular and cancer mortality among 64 913 adults. *BMJ Open Sport Exerc. Med.***5**, e000596 (2019).

[^10]: Lee, I.-M., Keadle, S. K. & Matthews, C. E. Fitness trackers to guide advice on activity prescription. *JAMA* **330**, 1733–1734 (2023).

[^11]: Ekelund, U., Sanchez-Lastra, M. A., Dalene, K. E. & Tarp, J. Dose-response associations, physical activity intensity and mortality risk: a narrative review. *J. Sport Health Sci.***13**, 24–29 (2024).

[^12]: Ahmadi, M. N. et al. Brief bouts of device-measured intermittent lifestyle physical activity and its association with major adverse cardiovascular events and mortality in people who do not exercise: a prospective cohort study. *Lancet Public Health* **8**, e800–e810 (2023).

[^13]: Stamatakis, E. et al. Association of wearable device-measured vigorous intermittent lifestyle physical activity with mortality. *Nat. Med.***28**, 2521–2529 (2022).

[^14]: Biddle, S. J. H. & Batterham, A. M. High-intensity interval exercise training for public health: a big HIT or shall we HIT it on the head? *Int. J. Behav. Nutr. Phys. Act.***12**, 95 (2015).

[^15]: LaCroix, A. Z. et al. Association of light physical activity measured by accelerometry and incidence of coronary heart disease and cardiovascular disease in older women. *JAMA Netw. Open* **2**, e190419 (2019).

[^16]: Besson, H., Brage, S., Jakes, R. W., Ekelund, U. & Wareham, N. J. Estimating physical activity energy expenditure, sedentary time, and physical activity intensity by self-report in adults. *Am. J. Clin. Nutr.***91**, 106–114 (2010).

[^17]: Haskell, W. L. Physical activity by self-report: a brief history and future issues. *J. Phys. Act. Health* **9**, S5–S10 (2012).

[^18]: Chastin, S. F. M. et al. How does light-intensity physical activity associate with adult cardiometabolic health and mortality? Systematic review with meta-analysis of experimental and observational studies. *Br. J. Sports Med.***53**, 370–376 (2019).

[^19]: Amagasa, S. et al. Associations of sedentary and physically-active behaviors with cognitive-function decline in community-dwelling older adults: compositional data analysis from the NEIGE study. *J. Epidemiol.***30**, 503–508 (2020).

[^20]: Ekelund, U. et al. Dose-response associations between accelerometry measured physical activity and sedentary time and all cause mortality: systematic review and harmonised meta-analysis. *BMJ* **366**, l4570 (2019).

[^21]: Ku, P., Hamer, M., Liao, Y., Hsueh, M. & Chen, L. Device-measured light-intensity physical activity and mortality: a meta-analysis. *Scand. J. Med Sci. Sports* **30**, 13–24 (2020).

[^22]: Doherty, C., Baldwin, M., Keogh, A., Caulfield, B. & Argent, R. Keeping pace with wearables: a living umbrella review of systematic reviews evaluating the accuracy of consumer wearable technologies in health measurement. *Sports Med.* 1–20 [https://doi.org/10.1007/s40279-024-02077-2](https://doi.org/10.1007/s40279-024-02077-2) (2024).

[^23]: Lim, W. K. et al. Beyond fitness tracking: the use of consumer-grade wearable data from normal volunteers in cardiovascular and lipidomics research. *PLoS Biol.***16**, e2004285 (2018).

[^24]: Google. Activity data types | Google Fit | Google for Developers. [https://developers.google.com/fit/datatypes/activity](https://developers.google.com/fit/datatypes/activity) (2024).

[^25]: Doherty, A. et al. Large scale population assessment of physical activity using wrist worn accelerometers: the UK Biobank study. *PLos One* **12**, e0169649 (2017).

[^26]: López-Bueno, R., Ahmadi, M., Stamatakis, E., Yang, L. & Del Pozo Cruz, B. Prospective associations of different combinations of aerobic and muscle-strengthening activity with all-cause, cardiovascular, and cancer mortality. *JAMA Intern Med.***183**, 982–990 (2023).

[^27]: Lee, D. H. et al. Long-term leisure-time physical activity intensity and all-cause and cause-specific mortality: a prospective cohort of US adults. *Circulation* **146**, 523–534 (2022).

[^28]: Wen, C. P. et al. Minimum amount of physical activity for reduced mortality and extended life expectancy: a prospective cohort study. *Lancet* **378**, 1244–1253 (2011).

[^29]: Scholes, S. et al. Age- and sex-specific criterion validity of the health survey for England physical activity and sedentary behavior assessment questionnaire as compared with accelerometry. *Am. J. Epidemiol.***179**, 1493–1502 (2014).

[^30]: Rutter, C. E., Millard, L. A. C., Borges, M. C. & Lawlor, D. A. Exploring regression dilution bias using repeat measurements of 2858 variables in ≤49 000 UK Biobank participants. *Int. J. Epidemiol.***52**, 1545–1556 (2023).

[^31]: Wewege, M., van den Berg, R., Ward, R. E. & Keech, A. The effects of high-intensity interval training vs. moderate-intensity continuous training on body composition in overweight and obese adults: a systematic review and meta-analysis. *Obes. Rev.***18**, 635–646 (2017).

[^32]: Stamatakis, E. et al. Vigorous intermittent lifestyle physical activity and cancer incidence among nonexercising adults: the UK biobank accelerometry study. *JAMA Oncol.***9**, 1255–1259 (2023).

[^33]: Peter-Marske, K. M. et al. Association of accelerometer-measured physical activity and sedentary behavior with incident cardiovascular disease, myocardial infarction, and ischemic stroke: the Women’s Health Study. *J. Am. Heart Assoc.***12**, e028180 (2023).

[^34]: Luo, M., Yu, C., Del Pozo Cruz, B., Chen, L. & Ding, D. Accelerometer-measured intensity-specific physical activity, genetic risk and incident type 2 diabetes: a prospective cohort study. *Br. J. Sports Med.***57**, 1257–1264 (2023).

[^35]: Tarp, J. et al. Accelerometer-measured physical activity and sedentary time in a cohort of US adults followed for up to 13 years: The influence of removing early follow-up on associations with mortality. *Int. J. Behav. Nutr. Phys. Act.***17**, 1–8 (2020).

[^36]: Mattioni Maturana, F., Martus, P., Zipfel, S. & NIEß, A. M. Effectiveness of HIIE versus MICT in improving cardiometabolic risk factors in health and disease: a meta-analysis. *Med Sci. Sports Exerc* **53**, 559–573 (2021).

[^37]: Leal, J. M., Galliano, L. M. & Del Vecchio, F. B. Effectiveness of high-intensity interval training versus moderate-intensity continuous training in hypertensive patients: a systematic review and meta-analysis. *Curr. Hypertens. Rep.***22**, 26 (2020).

[^38]: Costa, E. C. et al. Effects of high-intensity interval training versus moderate-intensity continuous training on blood pressure in adults with pre- to established hypertension: a systematic review and meta-analysis of randomized trials. *Sports Med.***48**, 2127–2142 (2018).

[^39]: Ahmadi, M. N. et al. Relationship of device measured physical activity type and posture with cardiometabolic health markers: pooled dose–response associations from the prospective physical activity, sitting and sleep consortium. *Diabetologia* **67**, 1051–1065 (2024).

[^40]: Martenstyn, J. A., Powell, L., Nassar, N., Hamer, M. & Stamatakis, E. Intensity-weighted physical activity volume and risk of all-cause and cardiovascular mortality: does the use of absolute or corrected intensity matter? *J. Phys. Act. Health* **16**, 1054–1059 (2019).

[^41]: Stamatakis, E. et al. Is cohort representativeness passé? Poststratified associations of lifestyle risk factors with mortality in the UK biobank. *Epidemiology* **32**, 179–188 (2021).

[^42]: Qiu, S. et al. Does objectively measured light-intensity physical activity reduce the risk of cardiovascular mortality? A meta-analysis. *Eur. Heart J. Qual. Care Clin. Outcomes* **7**, 496–504 (2021).

[^43]: Xie, B. et al. Accelerometer-measured light-intensity physical activity and the risk of cardiovascular disease or death in older adults: a meta-analysis. *Kardiol. Pol.***80**, 774–781 (2022).

[^44]: Rezende, L. F. M. et al. Lifestyle risk factors and all-cause and cause-specific mortality: assessing the influence of reverse causation in a prospective cohort of 457,021 US adults. *Eur. J. Epidemiol.***37**, 11–23 (2022).

[^45]: Ross, R. et al. Canadian 24-hour movement guidelines for adults aged 18–64 years and adults aged 65 years or older: an integration of physical activity, sedentary behaviour, and sleep. *Appl. Physiol. Nutr. Metab.***45**, S57–S102 (2020).

[^46]: Piercy, K. L. et al. The physical activity guidelines for Americans. *JAMA* **320**, 2020 (2018).

[^47]: Sipos, M., Paces, P., Rohac, J. & Novacek, P. Analyses of triaxial accelerometer calibration algorithms. *IEEE Sens J.***12**, 1157–1165 (2012).

[^48]: Ahmadi, M. N., Nathan, N., Sutherland, R., Wolfenden, L. & Trost, S. G. Non-wear or sleep? Evaluation of five non-wear detection algorithms for raw accelerometer data. *J. Sports Sci.***38**, 399–404 (2020).

[^49]: Moore, S. C. et al. Association of leisure-time physical activity with risk of 26 types of cancer in 1.44 million adults. *JAMA Intern Med*. **176**, 816–825 (2016).

[^50]: Conroy, M. C. et al. UK Biobank: a globally important resource for cancer research. *Br. J. Cancer* **128**, 519–527 (2023).

[^51]: Bakoyannis, G. & Touloumi, G. Practical methods for competing risks data: a review. *Stat. Methods Med Res*. **21**, 257–272 (2012).

[^52]: Desquilbet, L. & Mariotti, F. Dose-response analyses using restricted cubic spline functions in public health research. *Stat. Med*. **29**, 1037–1057 (2010).

[^53]: López-Bueno, R., Yang, L., Stamatakis, E. & Del Pozo Cruz, B. Moderate and vigorous leisure time physical activity in older adults and Alzheimer’s disease-related mortality in the USA: a dose-response, population-based study. *Lancet Healthy Longev.***4**, e703–e710 (2023).

[^54]: Carpenter, J. & Bithell, J. Bootstrap confidence intervals: when, which, what? A practical guide for medical statisticians. *Stat. Med*. **19**, 1141–1164 (2000).