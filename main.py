length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))
brand_name = input("Enter brand name: ")
customer_name = input("Enter customer name: ")

unit = input("Enter unit (mm/cm/inch): ").lower()
ply = int(input("Enter ply (3 or 5): "))
dimension = input("Enter dimension (inner(i)/outer(o)): ").lower()

flute_multiplier = {
        "a": 1.50,
        "b": 1.37,
        "c": 1.45,
        "e": 1.27
}

if unit == "cm":
    length *= 10
    breadth *= 10
    height *= 10
elif unit == "inch":
    length *= 25.4
    breadth *= 25.4
    height *= 25.4
elif unit != "mm":
    raise ValueError("Invalid unit")

if dimension == "i":
    if ply == 3:
        length += 5
        breadth += 5
        height += 5
    elif ply == 5:
        length += 8
        breadth += 8
        height += 8

deckle = breadth + height
sheet_length = 2 * (length + breadth) + 40
area = (deckle * sheet_length) / 1_000_000

total_price = 0
total_weight = 0

if ply == 3:
    gsm_top = float(input("Enter top GSM: "))
    gsm_flute = float(input("Enter flute GSM: "))
    gsm_bottom = float(input("Enter bottom GSM: "))

    paper_top = input("Top paper type: ").lower()
    paper_flute = input("Flute paper type: ").lower()
    paper_bottom = input("Bottom paper type: ").lower()

    flute_type = input("Flute type (a/b/c/e): ").lower()

    wt_top = (gsm_top * area) / 1000
    wt_bottom = (gsm_bottom * area) / 1000

    if flute_type not in flute_multiplier:
        raise ValueError("Invalid flute type")

    wt_flute = (gsm_flute * area * flute_multiplier[flute_type]) / 1000

    total_weight = wt_top + wt_flute + wt_bottom

    wastage = 1 + float(input("Enter wastage %: ")) / 100

    rate_top = float(input(f"Enter rate of {paper_top}: "))
    rate_flute = float(input(f"Enter rate of {paper_flute}: "))
    rate_bottom = float(input(f"Enter rate of {paper_bottom}: "))
    conversion_rate = float(input("Enter conversion rate: "))

    cost_top = wt_top * rate_top * wastage
    cost_flute = wt_flute * rate_flute * wastage
    cost_bottom = wt_bottom * rate_bottom * wastage
    cost_conversion = conversion_rate * total_weight

    total_price = cost_top + cost_flute + cost_bottom + cost_conversion
elif ply == 5:
    gsm_top = float(input("Enter top GSM: "))
    gsm_flute1 = float(input("Enter flute1 GSM: "))
    gsm_middle = float(input("Enter middle GSM: "))
    gsm_flute2 = float(input("Enter flute2 GSM: "))
    gsm_bottom = float(input("Enter bottom GSM: "))

    paper_top = input("Top paper type: ").lower()
    paper_flute1 = input("Flute1 paper type: ").lower()
    paper_middle = input("Middle paper type: ").lower()
    paper_flute2 = input("Flute2 paper type: ").lower()
    paper_bottom = input("Bottom paper type: ").lower()

    flute_type1 = input("Flute1 type (a/b/c/e): ").lower()
    flute_type2 = input("Flute2 type (a/b/c/e): ").lower()

    if flute_type1 not in flute_multiplier:
        raise ValueError("Invalid flute type")
    if flute_type2 not in flute_multiplier:
        raise ValueError("Invalid flute type")
    
    wt_top = (gsm_top * area) / 1000
    wt_flute1 = (gsm_flute1 * area * flute_multiplier[flute_type1]) / 1000
    wt_middle = (gsm_middle * area) / 1000
    wt_flute2 = (gsm_flute2 * area * flute_multiplier[flute_type2]) / 1000
    wt_bottom = (gsm_bottom * area) / 1000

    total_weight = wt_top + wt_flute1 + wt_middle + wt_flute2 + wt_bottom

    wastage = 1 + float(input("Enter wastage %: ")) / 100

    rate_top = float(input(f"Enter rate of {paper_top}: "))
    rate_flute1 = float(input(f"Enter rate of {paper_flute1}: "))
    rate_middle = float(input(f"Enter rate of {paper_middle}: "))
    rate_flute2 = float(input(f"Enter rate of {paper_flute2}: "))
    rate_bottom = float(input(f"Enter rate of {paper_bottom}: "))
    conversion_rate = float(input("Enter conversion rate: "))

    cost_top = wt_top * rate_top * wastage
    cost_flute1 = wt_flute1 * rate_flute1 * wastage
    cost_middle = wt_middle * rate_middle * wastage
    cost_flute2 = wt_flute2 * rate_flute2 * wastage
    cost_bottom = wt_bottom * rate_bottom * wastage
    cost_conversion = conversion_rate * total_weight

    total_price = cost_top + cost_flute1 + cost_middle + cost_flute2 + cost_bottom + cost_conversion

print("Total Price:", round(total_price, 2))
print("Total Weight x 960:", round(total_weight * 960, 2))

if paper_top == "kraft":
    KRAFT_FILL = "#b08953" 
elif paper_top == "virgin":
    KRAFT_FILL = "#d4a017" 
elif paper_top == "fbb":
    KRAFT_FILL = "#f5f6f2"
elif paper_top == "duplex":
    KRAFT_FILL = "#e6e2d6" 

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

def draw_rsc_kld_kraft(L, W, H, glue=40):

    plt.close('all')

    KRAFT_LINE = "#5C3A1E"
    TEXT_COLOR = "#2B1A0F"

    top_flap = W / 2
    bottom_flap = W / 2

    blank_length = 2 * (L + W) + glue
    blank_width = top_flap + H + bottom_flap

    panels = [L, W, L, W]

    fig = plt.figure(figsize=(14, 6))
    ax = fig.add_axes([0, 0, 1, 1])

    ax.set_xlim(-80, blank_length + 80)
    ax.set_ylim(-80, blank_width + 80)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.add_patch(
        Rectangle(
            (0, 0),
            blank_length,
            blank_width,
            facecolor=KRAFT_FILL,
            edgecolor="none"
        )
    )

    ax.add_patch(
        Rectangle(
            (0, 0),
            blank_length,
            blank_width,
            fill=False,
            linewidth=3,
            edgecolor=KRAFT_LINE
        )
    )

    x = glue
    ax.add_line(Line2D([x, x], [0, blank_width],
                       linestyle="--", color=KRAFT_LINE, linewidth=1.4))

    for p in panels[:-1]:
        x += p
        ax.add_line(Line2D([x, x], [0, blank_width],
                           linestyle="--", color=KRAFT_LINE, linewidth=1.4))

    ax.add_line(Line2D([0, blank_length], [bottom_flap, bottom_flap],
                       linestyle="--", color=KRAFT_LINE, linewidth=1.4))
    ax.add_line(Line2D([0, blank_length], [bottom_flap + H, bottom_flap + H],
                       linestyle="--", color=KRAFT_LINE, linewidth=1.4))

    x = glue
    for p in panels:
        ax.text(x + p/2, blank_width + 18, f"{int(p)} MM",
                ha='center', fontsize=10, weight='bold', color=TEXT_COLOR)
        x += p

    ax.text(glue/2, blank_width + 18, f"{glue} MM",
            ha='center', fontsize=10, weight='bold', color=TEXT_COLOR)

    ax.text(-55, bottom_flap/2, f"{int(bottom_flap)} MM",
            rotation=90, va='center', fontsize=10, weight='bold', color=TEXT_COLOR)
    ax.text(-55, bottom_flap + H/2, f"{int(H)} MM",
            rotation=90, va='center', fontsize=10, weight='bold', color=TEXT_COLOR)
    ax.text(-55, bottom_flap + H + top_flap/2, f"{int(top_flap)} MM",
            rotation=90, va='center', fontsize=10, weight='bold', color=TEXT_COLOR)

    ax.text(blank_length/2, blank_width + 50,
            f"RSC BLANK KLD ({int(L)}×{int(W)}×{int(H)} MM)",
            ha='center', fontsize=13, weight='bold', color=TEXT_COLOR)

    plt.show()

draw_rsc_kld_kraft(length, breadth, height)