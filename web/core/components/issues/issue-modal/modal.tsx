"use client";

import React from "react";
import { observer } from "mobx-react";
// types
import type { TIssue } from "@youtrack/types";
// components
import { CreateUpdateIssueModalBase } from "@/components/issues";
// constants
import { EIssuesStoreType } from "@/constants/issue";
// youtrack web providers
import { IssueModalProvider } from "@/youtrack-web/components/issues";

export interface IssuesModalProps {
  data?: Partial<TIssue>;
  isOpen: boolean;
  onClose: () => void;
  beforeFormSubmit?: () => Promise<void>;
  onSubmit?: (res: TIssue) => Promise<void>;
  withDraftIssueWrapper?: boolean;
  storeType?: EIssuesStoreType;
  isDraft?: boolean;
  fetchIssueDetails?: boolean;
  moveToIssue?: boolean;
  modalTitle?: string;
  primaryButtonText?: {
    default: string;
    loading: string;
  };
}

export const CreateUpdateIssueModal: React.FC<IssuesModalProps> = observer(
  (props) =>
    props.isOpen && (
      <IssueModalProvider>
        <CreateUpdateIssueModalBase {...props} />
      </IssueModalProvider>
    )
);
