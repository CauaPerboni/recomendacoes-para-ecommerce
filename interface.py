import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from recommendation_model import create_interaction_matrix, get_recommendations


class RecommendationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.df = pd.read_csv('retailrocket/events.csv')
        self.interaction_matrix_sparse, self.visitor_mapping, self.item_mapping = create_interaction_matrix(self.df)

        self.setWindowTitle('Recommendation System')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText('Enter User ID')
        self.layout.addWidget(self.user_input)

        self.recommend_button = QPushButton('Get Recommendations', self)
        self.recommend_button.clicked.connect(self.show_recommendations)
        self.layout.addWidget(self.recommend_button)

        self.result_label = QLabel('Recommendations will appear here', self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def show_recommendations(self):
        try:
            user_id = int(self.user_input.text())  
            if user_id not in self.visitor_mapping:
                self.result_label.setText(f"User ID {user_id} not found in the interaction matrix.")
            else:
                recommendations = get_recommendations(user_id, self.interaction_matrix_sparse, self.visitor_mapping, self.item_mapping)
                self.result_label.setText(f'Recommendations for User {user_id}: {recommendations}')
        except ValueError:
            self.result_label.setText("Please enter a valid User ID.")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecommendationApp()
    window.show()
    sys.exit(app.exec_())
