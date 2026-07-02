import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "FinAgent Rwanda | UI Library" },
      {
        name: "description",
        content:
          "Design mockups for FinAgent Rwanda: executive dashboard, transaction ledger, invoices & EBM receipts, and the tax compliance center.",
      },
    ],
  }),
  component: Index,
});

const SCREENS = [
  {
    title: "Executive Dashboard",
    description: "High-density KPIs, cashflow, and AI-assisted insights.",
    file: "executive_dashboard",
  },
  {
    title: "Transaction Ledger",
    description: "Zebra-striped, high-density transaction records.",
    file: "transaction_ledger",
  },
  {
    title: "Invoices & EBM Receipts",
    description: "Electronic billing machine invoices and receipts.",
    file: "invoices_ebm_receipts",
  },
  {
    title: "Tax Compliance Center",
    description: "Filing status, deadlines, and compliance tracking.",
    file: "tax_compliance_center",
  },
];

function Index() {
  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border">
        <div className="mx-auto max-w-5xl px-6 py-10">
          <p className="text-sm font-medium text-muted-foreground">FinAgent Rwanda</p>
          <h1 className="mt-1 text-3xl font-bold tracking-tight text-foreground">
            UI Library
          </h1>
          <p className="mt-2 max-w-2xl text-sm text-muted-foreground">
            Static design mockups exported from Stitch. Open any screen below to view
            it live.
          </p>
        </div>
      </header>

      <main className="mx-auto max-w-5xl px-6 py-10">
        <div className="grid gap-6 sm:grid-cols-2">
          {SCREENS.map((screen) => (
            <a
              key={screen.file}
              href={`/ui-library/${screen.file}.html`}
              className="group overflow-hidden rounded-lg border border-border bg-card transition-colors hover:border-ring"
            >
              <div className="aspect-video overflow-hidden bg-muted">
                <img
                  src={`/ui-library/${screen.file}.png`}
                  alt={`${screen.title} preview`}
                  loading="lazy"
                  className="h-full w-full object-cover object-top transition-transform duration-300 group-hover:scale-[1.02]"
                />
              </div>
              <div className="p-5">
                <h2 className="text-lg font-semibold text-card-foreground">
                  {screen.title}
                </h2>
                <p className="mt-1 text-sm text-muted-foreground">
                  {screen.description}
                </p>
              </div>
            </a>
          ))}
        </div>
      </main>
    </div>
  );
}
