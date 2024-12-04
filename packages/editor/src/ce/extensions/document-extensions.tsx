import { HocuspocusProvider } from "@hocuspocus/provider";
import { Extensions } from "@tiptap/core";
import { SlashCommands } from "@/extensions";
// youtrack editor types
import { TIssueEmbedConfig } from "@/youtrack-editor/types";
// types
import { TExtensions, TUserDetails } from "@/types";

type Props = {
  disabledExtensions?: TExtensions[];
  issueEmbedConfig: TIssueEmbedConfig | undefined;
  provider: HocuspocusProvider;
  userDetails: TUserDetails;
};

export const DocumentEditorAdditionalExtensions = (_props: Props) => {
  const extensions: Extensions = [SlashCommands()];

  return extensions;
};
