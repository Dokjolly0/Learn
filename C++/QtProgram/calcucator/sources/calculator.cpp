#include "../headers/calculator.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QDebug>

Calculator::Calculator(QWidget *parent)
    : QWidget(parent), leftOperand(0.0)
{
    display = new QLineEdit("0");
    display->setReadOnly(true);
    display->setAlignment(Qt::AlignRight);
    display->setMaxLength(15);

    layout = new QGridLayout;
    layout->addWidget(display, 0, 0, 1, 4);

    createButtons();

    setLayout(layout);
    setWindowTitle("Calculator");
}

void Calculator::createButtons()
{
    QStringList digitButtons = {"7", "8", "9", "4", "5", "6", "1", "2", "3", "0"};
    int pos = 0;
    for (int row = 1; row <= 4; ++row) {
        for (int col = 0; col < 3; ++col) {
            if (pos < digitButtons.size()) {
                layout->addWidget(createButton(digitButtons[pos], SLOT(onDigitButtonClicked())), row, col);
                ++pos;
            }
        }
    }

    layout->addWidget(createButton("C", SLOT(onClearButtonClicked())), 1, 3);
    layout->addWidget(createButton("/", SLOT(onOperatorButtonClicked())), 2, 3);
    layout->addWidget(createButton("*", SLOT(onOperatorButtonClicked())), 3, 3);
    layout->addWidget(createButton("-", SLOT(onOperatorButtonClicked())), 4, 3);
    layout->addWidget(createButton("+", SLOT(onOperatorButtonClicked())), 4, 2);
    layout->addWidget(createButton("=", SLOT(onEqualButtonClicked())), 4, 1);
}

QPushButton* Calculator::createButton(const QString &text, const char *member)
{
    QPushButton *button = new QPushButton(text);
    connect(button, SIGNAL(clicked()), this, member);
    return button;
}

void Calculator::onDigitButtonClicked()
{
    QPushButton *button = qobject_cast<QPushButton*>(sender());
    QString digitValue = button->text();
    QString currentValue = display->text();

    if (currentValue == "0") {
        display->setText(digitValue);
    } else {
        display->setText(currentValue + digitValue);
    }
}

void Calculator::onOperatorButtonClicked()
{
    QPushButton *button = qobject_cast<QPushButton*>(sender());
    pendingOperator = button->text();
    leftOperand = display->text().toDouble();
    display->setText("0");
}

void Calculator::onEqualButtonClicked()
{
    double rightOperand = display->text().toDouble();
    double result = 0.0;

    if (pendingOperator == "+") {
        result = leftOperand + rightOperand;
    } else if (pendingOperator == "-") {
        result = leftOperand - rightOperand;
    } else if (pendingOperator == "*") {
        result = leftOperand * rightOperand;
    } else if (pendingOperator == "/") {
        if (rightOperand > 0 || rightOperand < 0) {
            result = leftOperand / rightOperand;
        } else {
            display->setText("Error");
            return;
        }
    }

    display->setText(QString::number(result));
}

void Calculator::onClearButtonClicked()
{
    display->setText("0");
    pendingOperator.clear();
    leftOperand = 0.0;
}
