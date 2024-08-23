#include <QApplication>
#include "../headers/calculator.h"
#include <QIcon>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // Imposta l'icona dell'applicazione
    app.setWindowIcon(QIcon(":/icon.png"));

    Calculator calculator;
    calculator.show();
    return app.exec();
}
