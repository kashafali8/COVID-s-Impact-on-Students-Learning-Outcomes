# COVID's Impact on Students' Learning Outcomes

## Github Repository Details

This GitHub repository showcases two distinct projects. The first project was a collaborative effort aimed at measuring the impact of COVID-19 on students' learning outcomes. In contrast, the second project is an individual endeavor, serving as a replication study based on the original project but adopting a Bayesian approach for analysis and interpretation.

The design of the original causal inference study used a combination of difference-in-difference (Diff-in-Diff) and fixed effects (FE) to estimate the impact of the COVID-19 pandemic on academic achievement while controlling for unobserved variation across schools. While Diff-in-Diff was used to compare the change in mean test scores for females and males at the school level across different subject assessments before and after the pandemic and provides an estimate of the causal effect of the pandemic on female test scores, it may not account for unobserved variation between different schools. We added fixed effects at the school level to the Diff-in-Diff model as the fixed effects will capture the differences in the unobserved school-level characteristics that are constant over time. 

The replication study contributed to the research design in three essential ways: (i) replicated the existing fixed effects model using a Bayesian Approach, (ii) identified and removed Science Assessment outliers in the data and (iii) introduced a bayesian hierarchical model as an innovative statistical approach to answer this research question.

## Motivation

It is no secret that the Covid-19 pandemic affected every sector of human civilization humanly imaginable, and we decided to focus specifically on Covid-19’s long-term effects on the educational outcomes across genders in the New York school system. Pandemic regulations and online learning modalities stressed the educational system and affected student well-being. As students were returning to school and were studying online as well, they faced an amalgamation of issues such as social isolation, increased anxiety, and strong familial and financial instability. When considering this information, we devoted our attention to quantifying this impact under a gendered lens, given that we also know how females are impacted in a more nuanced way during public health emergencies.

The goal is to answer the following main research question in both studies: What is the causal effect of the Covid-19 pandemic on students' test scores by gender in New York City?

## Project Dataset

Both studies used the same [Report Card datasets](https://data.nysed.gov/downloads.php) from the official website of the New York State Education Department for four academic years, namely, 2017-2018, 2018-2019, 2020-2021, and 2021-2022 to understand our problem. These datasets are at the school-level and provide information on mean school results for ELA, Math, and Science assessments at the elementary and intermediate-level, as well as contain mean school assessment results for different groups like gender, race and others. Since this is a panel dataset, it offers information regarding assessment scores from the same schools before and after the COVID-19 pandemic outbreak. We observed pre-pandemic and post-pandemic mean test scores by gender and subject, and other demographic variables such as race, and whether English is their first language for different schools in New York.

## Original Project Results - A Non-Bayesian Approach (Group Project)

We employed a fixed effects model using the frequentist approach at the school level to account for variations both across schools and over time. The initial findings underscored a noteworthy performance gap between genders: prior to the pandemic, females consistently outperformed males by approximately 3 mean score points across the subjects examined. However, when examining the interplay of how the pandemic’s effects varied academic performance by gender in the fixed effect model, it was evident that the presence of the pandemic led to a decrease of 1.36 mean score points larger for females when compared to males. This signifies, that although females perform better than their male counterparts in terms of academic performance, the pre-existing gap between them was narrowed due to how females reacted to the pandemic.

## Replication Study - A Bayesian Approach (Individual Project)

This replication study allowed me to replicate a fixed effects model from a Bayesian approach to highlight how females, who were performing better than their male counterparts in school before the pandemic, were affected more by the pandemic than males. While these results remained consistent in a Bayesian fixed effects model, an extension to the study also allowed me to further dive into school-level effects using a hierarchical model. Results from the hierarchical model further corroborated the original study’s results, but also added that schools which were performing worse than average before the pandemic were affected more by the pandemic than schools which were performing better. This trend continues to hold for both females and males, and females in low performance schools were impacted more than females in high performance school post-pandemic.
