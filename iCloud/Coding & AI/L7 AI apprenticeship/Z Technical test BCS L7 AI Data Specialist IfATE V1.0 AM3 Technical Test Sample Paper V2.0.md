---
tags:
  - EPA
  - AM3
  - technical-test
  - BCS
  - L7
source: BCS Level 7 Artificial Intelligence Data Specialist IfATE V1.0 AM3 Sample Paper V2.0
date: June 2024
---

# BCS Level 7 – Artificial Intelligence Data Specialist Apprenticeship
## Assessment Method 3 – Technical Test Sample Paper

> *This is a United Kingdom government regulated qualification which is administered and approved by one or more of the following: Ofqual, Qualifications Wales, CCEA Regulation or SQA.*

---

## Change History

| Version & Date | Changes Made |
|---|---|
| V1.0 – October 2021 | Document created. |
| V1.1 – August 2023 | Document updated. |
| V2.0 – June 2024 | New template applied (no content changes). |

---

## Technical Test Format

This sample paper comprises a scenario, followed by **4 technical questions** based on the scenario.

The apprentice has **100 minutes** to answer the 4 questions.

> [!warning] Copyright
> Copying of this paper is expressly forbidden without the direct approval of BCS, The Chartered Institute for IT.

---

## Scenario

The vision of a multi-site, nationwide grocery retailer is to **"Find the simplest way to feed the nation's families."**

The continuous improvement (CI) team have suggested that transforming all branches into an entirely **till-less experience** would be the best way to fulfil the organisation's vision of simplifying the shopping process, while still maintaining a strong bricks and mortar presence, allowing customers to simply **"lift and leave"** with their goods.

> [!info] Your Role
> **Your role is to recommend a solution which will make the most of the processes being automated by:**
> Predicting who will be shopping and what they will be purchasing to ensure the correct stock levels in store and making the checkout process as seamless as possible.

---

### Payments

Currently, customers have the option to shop and checkout in three ways:

- **Traditional till checkout** – A manual scan till operated by a store employee with no customer input other than payment. Cash, card and contactless payments available.
- **Self-checkout** – A limited function, manual scan till operated by the customer, with employee input only for approving the sale of age-restricted products or rectifying errors. Card and contactless payments only.
- **Self-scan** – A hand-held scanner is used by the customer to scan each item as they add it to their basket. This scanner is then docked, and payment is made at the docking station, with employee input only for approving the sale of age-restricted products or rectifying errors. Card and contactless payments only.

---

### Stock Control

Due to the high-accuracy level of the system in use, stock is currently received on a **"good faith" delivery basis** from the organisation's central warehouse — only **15%** of the delivery is manually checked upon receipt.

The stock control system **FoodTrack** is updated via a virtual stock transfer on the day of delivery from the central distribution centre. Any items missing or damaged upon delivery may be manually corrected.

Most items are currently processed through the till system **CheckoutTrack** via a barcode printed onto their packaging, with loose items such as vegetables being manually entered from a touch screen menu of choices.

CheckoutTrack transactions update stock levels on FoodTrack at least every **90 minutes** during store opening hours (6am–11pm), and a full comparison/update is completed between **12 midnight and 4am** every day.

Each product has a **"trigger" stock level** which, when reached, will automatically add that product onto the next order for delivery. Trigger levels vary across branches to account for different customer demographics and geographical differences.

---

### Technology

The organisation has been using **CheckoutTrack** and **FoodTrack** software for many years — both customers and employees are familiar with its interface.

Self-checkout and self-scan both required significant investment, however a notable proportion of this was balanced by salary savings from employing fewer checkout operators.

Discussions around till-free technology, customer tracking and stock control have generated suggestions such as:

- Weighted shelves
- Facial recognition
- Fingerprint recognition
- Mobile applications

---

### Requirements

The following requirements have been elicited from the project team:

- [ ] We must be able to link all customers who enter the store with a valid ID.
- [ ] Means to pay must be established before goods are removed from the store.
- [ ] All items removed from the store must be recorded to maintain accurate stock level data.
- [ ] No extended delays to existing goods-in or replenishment processes shall occur.
- [ ] We shall be able to predict which products are required by store/time.
- [ ] We shall be able to make predictions of which additional products we should stock for customers to purchase.

---

### Challenges

Some key considerations of the CI team have been:

- A trial has previously taken place in which staff members could scan their own goods using a mobile application with a saved payment method and leave the store with no further checks. However, there were **concerns around lack of traceability and potential for fraud**.
- Around **40%** of the current workforce are employed as checkout operators (or related roles).
- A **customer membership scheme** exists, which provides customers with members-only offers based on their purchase history. This is currently activated by the customer scanning their membership card at their chosen payment point. This data is recorded on **MemberTrack**.
- **Service-related customer complaints have risen** since the introduction of self-checkouts and self-scan over the last 5 years.
- **CCTV** is in place in all stores but is limited to visual recordings only.

> Your suggestions and findings shall be presented to the board, which is comprised of members with varying levels of technical knowledge.

---

## Data Sources Reference

### External Data Sources

| Source | Description | Use |
|---|---|---|
| **Consumer Confidence Index** | Tracks and predicts customer spending habits and the state of the economy as a whole | Influences budgets and stock purchasing |
| **Office of National Statistics** | Identifies the customer demographic within each store location | Identifies potential new customer members; assists with planning stock ranges for new stores |
| **MetOffice** | Identifies weather patterns and geographical differences which can impact customer buying habits | Assists with delivery planning and stock ranges for new stores |

*\*External data sources include but are not limited to the examples provided.*

### Internal Data Sources

```
┌─────────────────────────────────────────────────────────────────┐
│                     Internal Data Cycle                         │
│                                                                 │
│   MemberTrack          ──────►         FoodTrack                │
│   ─────────────                        ─────────                │
│   Members' personal                    Current & ideal          │
│   information and                      stock levels per         │
│   purchase history.                    item, by store.          │
│                                                                 │
│   Used to generate                     Also stores stock        │
│   promotions and                       at distribution          │
│   targeted marketing.                  centre & expiration      │
│                                        dates of perishables.    │
│   Feeds into FoodTrack                                          │
│   for promotional stock.               Used to plan             │
│                         ◄──────        deliveries.              │
│                                                                 │
│              CheckoutTrack                                      │
│              ──────────────                                     │
│   Generates data around customer transactions and payment,      │
│   including items purchased, payment method, discounts          │
│   applied and membership status.                                │
│   Feeds into FoodTrack and MemberTrack.                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technical Test Questions

> [!tip] Format
> 4 questions | 100 minutes total

---

### Question 1 – Data Extraction, Linkage & Uncertainty

**a)** Identify the types of data you shall use to complete the tasks described in the scenario.

**b)** Describe your process for extracting the data.

**c)** Explain how data from multiple systems can be linked to meet business objectives.

**d)** Within your chosen data sets and sources, explain the potential for:
- Error
- Bias
- Uncertainty

**e)** Explain the differences between the types of uncertainty associated with the outputs of both data collection and data analysis. Include a comparison of uncertainty in data before and after analysis.

> [!note] Knowledge & Skills Assessed
> - **K4**: How to extract data from systems and link data from multiple systems to meet business objectives.
> - **K24**: Sources of error and bias, including how they may be affected by choice of dataset and methodologies applied.
> - **S21**: Identify and quantify different kinds of uncertainty in the outputs of data collection, experiments and analyses.

---

### Question 2 – Storage, Analysis & Machine Learning

**a)** Explain how the extracted data can be stored, analysed and visualised.

**b)** Describe the storage requirements of the data you have gathered.

**c)** Justify the reasons for your proposed storage solutions and processing technologies.

**d)** Explain how your intended solution will make use of the data by comparing a choice of **two or more machine learning algorithms and approaches** which you may apply to present the best solution for the organisation.

> [!note] Knowledge & Skills Assessed
> - **K2**: How to apply modern data storage solutions, processing technologies and machine learning methods to maximise the impact to the organisation by drawing conclusions from applied research.
> - **K20**: How to collect, store, analyse and visualise data.

---

### Question 3 – Legal, Ethical & Social Impact

**a)** Through analysis of internal and external business factors:
- Identify the constraints affecting your solution.
- Explain the internal and external impact of implementation from a **legal, social, ethical and professional** perspective.

> [!note] Knowledge & Skills Assessed
> - **K9**: The current or future legal, ethical, professional and regulatory frameworks which affect the development, launch and ongoing delivery and iteration of data products and services.
> - **K12**: The wider social context of AI, data science and related technologies, to assess business impact of current ethical issues such as workplace automation and misuse of data.

---

### Question 4 – Design, Development & Deployment

**a)** Explain the approach you would take to design, develop and deploy your AI and data science solution.

**b)** List the resources and architecture required.

**c)** Provide justification for your approach.

> [!note] Knowledge & Skills Assessed
> - **K15**: The engineering principles used (general and software) to investigate and manage the design, development and deployment of new data products within the business.
> - **K27**: The engineering principles used (general and software) to create new instruments and applications for data collection.
> - **S13**: Identify appropriate resources and architectures for solving a computational problem within the workplace.

---

*Copyright © BCS 2024*
