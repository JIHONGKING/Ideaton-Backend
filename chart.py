import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일 경로 설정
file_path = '/Users/jihong/Desktop/아이디어톤/Acceptance Rate by Experience( JOB SEEKER)/sample_experience_acceptance_improved.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 사용자 입력: 현재 지원자의 경력, 합격률, 회사 이름 (예시: 10년 경력, 65% 합격률, 'Company A')
current_experience = 10.0
current_acceptance_rate = 65.0
current_company = 'Company A'

# Filter the DataFrame to include only applicants from the specified company
filtered_df = df[df['Primary Company'] == current_company]

# Scatter plot and trend line for the filtered data
fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(filtered_df['Experience'], filtered_df['Acceptance Rate'], color='blue', alpha=0.7, label=f'{current_company} Applicants')

# Adding current applicant's data point
current_point = ax.scatter(current_experience, current_acceptance_rate, color='magenta', s=100, label='Current Applicant')

# Adding trend line
if not filtered_df.empty:
    z = np.polyfit(filtered_df['Experience'], filtered_df['Acceptance Rate'], 1)
    p = np.poly1d(z)
    ax.plot(filtered_df['Experience'], p(filtered_df['Experience']), color='red', linestyle='-', linewidth=1, label='Trend Line')

# Adding labels and title
ax.set_xlabel('Experience (Years)')
ax.set_ylabel('Acceptance Rate (%)')
ax.set_title('Acceptance Rate by Experience')
ax.set_ylim(0, 100)  # Set y-axis limits to 0-100%
ax.legend()
ax.grid(True)

# Adding annotation for mouse hover and click
annot = ax.annotate("", xy=(0,0), xytext=(20,20),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    experience = pos[0]
    acceptance_rate = pos[1]
    other_companies = df[(df['Experience'] == experience) & (df['Acceptance Rate'] == acceptance_rate)]['Other Companies'].values[0]
    annot.xy = pos
    text = f"Experience: {experience:.2f} years\nAcceptance Rate: {acceptance_rate:.2f}%\nOther Companies: {other_companies}"
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            cont, ind = current_point.contains(event)
            if cont:
                annot.xy = (current_experience, current_acceptance_rate)
                annot.set_text(f"Current Position\nExperience: {current_experience:.2f} years\nAcceptance Rate: {current_acceptance_rate:.2f}%")
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

def click(event):
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            cont, ind = current_point.contains(event)
            if cont:
                annot.xy = (current_experience, current_acceptance_rate)
                annot.set_text(f"Current Position\nExperience: {current_experience:.2f} years\nAcceptance Rate: {current_acceptance_rate:.2f}%")
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)
fig.canvas.mpl_connect("button_press_event", click)

plt.show()
