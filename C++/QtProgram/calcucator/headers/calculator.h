#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QGridLayout>

class Calculator : public QWidget
{
    Q_OBJECT

public:
    Calculator(QWidget *parent = nullptr);

private slots:
    void onDigitButtonClicked();
    void onOperatorButtonClicked();
    void onEqualButtonClicked();
    void onClearButtonClicked();

private:
    QLineEdit *display;
    QGridLayout *layout;
    QString pendingOperator;
    double leftOperand;

    void createButtons();
    QPushButton* createButton(const QString &text, const char *member);
};

#endif // CALCULATOR_H
