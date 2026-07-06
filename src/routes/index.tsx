import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  beforeLoad: () => {
    throw redirect({ href: "/ui-library/executive_dashboard.html" });
  },
  component: () => null,
});
