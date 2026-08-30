# Goes Market and Household Economy 1585–1602

**World ID:** `WORLD.GOES_MARKET_HOUSEHOLD_1585_1602`  
**Status:** ACTIVE_AUTHORING_REFERENCE  
**Role:** late-life local calibration and transaction-mechanism layer  
**Authority:** subordinate to canon and current Story Claims

This layer prevents a common historical-writing error: treating every monetary amount in a notarial record as if it were the same kind of `price`.

The late Goese evidence instead preserves several distinct economic forms:

`market transaction | estate valuation | payment in kind | accumulated debt | tax/impost rule | quality rejection | transport tariff`

They must remain separate in authoring and in any future calculator.

---

## 1. Rye: price is a dated transaction, not an annual constant

A late-1595 Goese attestation reconstructs actual earlier purchases by local grain buyers:

- April 1595: `£26 Vlaams per last`;
- May 1595: `14 schellingen 2 groten per sack`, stated as `£26 11 schellingen 3 groten per last`;
- around 17–18 August 1595: `£19 Vlaams per last`.

This is a direct lesson in **intra-year volatility**. A scene should ask *when* grain was bought, not merely *what rye cost in 1595*.

The May 14s2g figure is not an October spot price; it is a transaction recalled in the later attestation.

Evidence: `SC.HIST.GOES.RYE_PRICE.1595.001`.

---

## 2. Payment in kind: Spanish-leather shoes, 1597

On 10 February 1597 a Goese professional-service payment was settled with:

- one pair of new shoes;
- Spanish leather;
- reckoned at `6 schellingen groten`.

Authoring classification:

`IN_KIND_PAYMENT / OBJECT_VALUATION`

This permits a money economy in which obligations do not always end with coins changing hands. A valued object can discharge a fee.

Do **not** turn `6 schellingen` into `the price of shoes in Goes in 1597`. The record concerns one specified pair in one settlement.

Evidence: `SC.HIST.GOES.FOOTWEAR.INKIND_PAYMENT.1597.001`.

---

## 3. Imported food, sensory expertise and rejection: fish, 1598

On 12 December 1598 **Jan Jansz Nissepadt** appears as sworn fish inspector of Goes.

The transaction involved:

- four barrels of imported `Aberdaens` fish;
- transport to the Goese auction by a Zierikzee boatman;
- inspection by the sworn inspector;
- practical assistance from two experienced female fish sellers, Nele Mercx and Nelle Jacobs;
- a finding that the fish was insufficiently salted and partly mouldy, rotten and foul-smelling;
- notarial documentation to support rejection/cancellation against the seller.

This is a particularly useful micro-economic mechanism because quality is determined materially and socially, not by an abstract price list.

Authoring chain:

`ship/barrel -> auction -> opening/smell/texture -> sworn inspector -> experienced sellers -> rejection -> notarial proof -> claim against supplier`

### Nissepadt identity guardrail

The source proves this named historical office-holder. It does not prove that every Jan Nissepat/Nissepadt reference in the project is the same man.

Evidence: `SC.HIST.GOES.FISH.QUALITY_INSPECTION.NISSEPADT.1598.001`.

---

## 4. Meat: sale place and tax point need not coincide, 1598

A 22 December 1598 attestation describes a butcher who:

- slaughtered sheep, cows, oxen and cattle in Heinkenszand;
- carried the meat into Goes;
- sold it publicly near the meat hall;
- sold `bij den ponde, stucke ende leden` — by pound, piece and cuts/limbs.

The witness said that the impost had already been paid where `the blood was shed`, Heinkenszand, and was therefore not charged again by the Goese impost farmers.

Authoring consequence:

`place of production/slaughter != place of sale != automatically a second tax point`

The record gives no rate. It should be used as an attested transaction/jurisdiction mechanism, not as a universal meat-tax code.

Evidence: `SC.HIST.GOES.MEAT.IMPOST_TAXPOINT.1598.001`.

---

## 5. Household value: butter in a sterfhuis inventory, 1602

A Goese estate inventory dated 20 November 1602 records:

- `78 pond` butter;
- taken over by the woman of the house;
- at `4 stuivers per pond`.

Authoring classification:

`ESTATE_TAKEOVER_VALUATION`

This is a real local late-life monetary anchor, but not automatically an open-market retail quote. Estate valuation can reflect negotiated takeover, appraisal practice, condition and context.

The same inventory is useful beyond the single number because it shows a household as an **inventory of valued material life**: clothing, bedding, furniture, tools, vessels, food stock and mixed monetary/property claims can all acquire recorded values after death.

Evidence: `SC.HIST.GOES.HOUSEHOLD.BUTTER_VALUATION.1602.001`.

### Nissepadt executor

The inventory names **Henri/Henric Adriaens Nissepadt** as executor of the deceased's testament.

This is a significant historical Nissepadt reference, but identity with another project-tracked Hendrick/Henric Adriaensz Nissepat remains **UNRESOLVED** until genealogy, offices, property or other records bridge the names.

Evidence: `SC.HIST.GOES.NISSEPADT.HENRIC_EXECUTOR.1602.001`.

---

## 6. Food can be labour infrastructure: South-Beveland, 1599

A nearby 1599 dike-work dispute records food supplied to labourers on credit during work on the breached Poppendijk:

- bread;
- cheese;
- butter;
- bacon;
- herring.

The surviving evidence gives aggregate debts and collection trouble rather than useful unit prices.

Authoring value is therefore not `what one herring cost`, but the mechanism:

`emergency work -> labour concentration -> local shopkeeper supplies food -> running credit -> aggregate debt -> collection conflict`

Classification: `CLOSE_REGIONAL_PROVISIONING_CONTEXT`, not direct Goes pricing.

Evidence: `SC.HIST.SOUTH_BEVELAND.DIKE_PROVISIONING.FOOD_CREDIT.1599.001`.

---

## 7. Classification table

| Evidence | Correct class | What it can support | What it cannot support |
|---|---|---|---|
| rye purchases 1595 | `TRANSACTION_PRICE_SEQUENCE` | dated commodity prices and volatility | one fixed annual rye price |
| shoes 1597 | `IN_KIND_PAYMENT / OBJECT_VALUATION` | goods settling professional fees | generic shoe retail price |
| fish 1598 | `QUALITY_INSPECTION / RESCISSION` | spoilage, expertise, market enforcement | fish price without a stated price |
| meat 1598 | `IMPOST_TAXPOINT / SALE_UNIT` | tax-place dispute; pound/piece/cut retailing | an impost rate |
| butter 1602 | `ESTATE_TAKEOVER_VALUATION` | local household valuation | automatic market-stall price |
| dike food 1599 | `CLOSE_REGIONAL_PROVISIONING_CONTEXT` | labour provisioning on credit | Goese unit prices |

---

## 8. Hard guardrails

1. `amount in a document` does not automatically mean `market price`.
2. Keep market transaction, valuation, debt, tax, wage, freight and in-kind settlement separate.
3. The May 1595 rye price is not an October spot price.
4. The 1602 butter figure is an estate takeover valuation.
5. The 1597 shoe figure is an in-kind settlement/object valuation.
6. The 1598 meat evidence gives an attested tax point, not a tax rate.
7. The fish record gives quality/rejection evidence, not a fish price.
8. Similar Nissepat/Nissepadt names are not automatically the same historical person.
9. South-Beveland evidence remains regional context when it is not from Goes itself.
10. None of these historical persons or transactions creates fictional participation by Claes.

---

## 9. Linked evidence

- `claims/SOURCE_CLAIMS_ECONOMY_2026-08-30.yaml`
- `claims/SOURCE_CLAIMS_GOES_MARKET_HOUSEHOLD_2026-08-30.yaml`
- `sources/SRC-SECONDARY-LEVENDale-GOES-NOTARIAL-COMPILATION-001.md`
- `storybible/domains/GOES_ECONOMIC_BASELINE_1542_1572.md`
- `narrative/economic_state_resolver.yaml`

This domain is a reference layer. It does not itself establish that Claes bought, sold, inspected, inherited, owed or paid any of the documented goods or sums.
